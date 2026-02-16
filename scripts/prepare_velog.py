import os
from sync_utils import load_hugo_post, transform_image_urls, GITHUB_PAGES_BASE

# Configuration
SOURCE_DIR = 'content/ko/posts'
DEST_DIR = 'velog_dist'

def convert_to_velog(file_path, filename):
    post = load_hugo_post(file_path)
    content = post.content
    
    # 1. FIX IMAGES: Convert relative paths to Absolute GitHub URLs
    content = transform_image_urls(content, GITHUB_PAGES_BASE)

    # 2. ADD FOOTER (Canonical Link)
    # Good for SEO: Tells Google the GitHub version is the original
    original_url = f"{GITHUB_PAGES_BASE}/ko/posts/{filename.replace('.md', '')}/"
    footer = f"\n\n---\n*원문은 [제 개인 블로그]({original_url})에 게시된 글입니다.*"
    content += footer

    # 3. SAVE (Ready to Copy-Paste)
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        
    with open(os.path.join(DEST_DIR, filename), 'w', encoding='utf-8') as f:
        # We don't save Frontmatter because Velog UI handles title/tags separately
        # We just save the body for easy copying.
        f.write(content)
        
    print(f"✅ Ready for Velog: {filename}")

def main():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.md'):
            convert_to_velog(os.path.join(SOURCE_DIR, filename), filename)

if __name__ == "__main__":
    main()

