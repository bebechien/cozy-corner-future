import os
import re
import frontmatter # pip install python-frontmatter

# Configuration
SOURCE_DIR = 'content/ko/posts'
DEST_DIR = 'velog_dist'
# Your GitHub Pages URL (Where images are hosted)
GITHUB_PAGES_URL = "https://bebechien.github.io/cozy-corner-future"

def convert_to_velog(file_path, filename):
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)

    content = post.content
    
    # 1. FIX IMAGES: Convert relative paths to Absolute GitHub URLs
    # Matches: ![alt](/images/foo.png) or ![alt](images/foo.png)
    # Replaces with: ![alt](https://.../images/foo.png)
    def image_replacer(match):
        alt_text = match.group(1)
        img_path = match.group(2)
        
        # If it's already an external URL, leave it alone
        if img_path.startswith('http'):
            return match.group(0)
            
        # Clean the path (remove leading slash)
        clean_path = img_path.lstrip('/')
        
        return f'![{alt_text}]({GITHUB_PAGES_URL}/{clean_path})'

    # Regex search for Markdown images
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', image_replacer, content)

    # 2. ADD FOOTER (Canonical Link)
    # Good for SEO: Tells Google the GitHub version is the original
    original_url = f"{GITHUB_PAGES_URL}/ko/posts/{filename.replace('.md', '')}/"
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

