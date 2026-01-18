import os
import re
import frontmatter # pip install python-frontmatter
import yaml

# --- CONFIGURATION ---
SOURCE_DIR = 'content/en/posts'
DEST_DIR = 'devto_dist/posts'
# Your GitHub Pages URL (Source of Truth)
GITHUB_PAGES_BASE = "https://bebechien.github.io/cozy-corner-future"

def prepare_post(file_path, filename):
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)

    # 1. Map Hugo metatdata to DEV.to metadata
    devto_metadata = {
        'title': post.get('title', 'No Title'),
        'description': post.get('description', ''),
        'tags': post.get('tags', []),
        'cover_image': f"'{GITHUB_PAGES_BASE}/{post['cover']}'" if post.get('cover') else '',
        'published': not post.get('draft', False),
    }

    # Auto-generate Canonical URL (Critical for SEO)
    # Assumes Hugo URL structure: base/en/posts/filename/
    slug = filename.replace('.md', '')
    if 'url' in post.metadata:
        slug = post.metadata['url'].strip('/')
    
    canonical = f"{GITHUB_PAGES_BASE}/en/posts/{slug}/"
    post['canonical_url'] = canonical

    # 2. CONTENT TRANSFORMATION (Image Paths)
    # Converts ![alt](/images/foo.png) -> ![alt](https://.../images/foo.png)
    content = post.content
    
    def image_replacer(match):
        alt_text = match.group(1)
        img_path = match.group(2)
        
        if img_path.startswith('http'):
            return match.group(0)
            
        # Remove leading slash
        clean_path = img_path.lstrip('/')
        
        return f'![{alt_text}]({GITHUB_PAGES_BASE}/{clean_path})'

    # Regex for standard Markdown images
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', image_replacer, content)

    # 3. WRITE TO DIST FOLDER
    output_path = os.path.join(DEST_DIR, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        yaml.dump(devto_metadata, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n")
        f.write(content)
    
    print(f"✅ Formatted for DEV.to: {filename}")

def main():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.md'):
            prepare_post(os.path.join(SOURCE_DIR, filename), filename)

if __name__ == "__main__":
    main()
