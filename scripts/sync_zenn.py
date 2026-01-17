import os
import frontmatter # Requires: pip install python-frontmatter
import yaml
import re

# Configuration
SOURCE_DIR = 'content/ja/posts' # Your Hugo Japanese content
DEST_DIR = 'articles'           # Zenn's articles directory

def zenn_slugify(filename):
    """
    Zenn requires slugs to be 12-50 characters, lowercase, a-z, 0-9, -, _.
    If your Hugo filename is too short, we append a suffix or you must rename it.
    """
    slug = os.path.splitext(filename)[0]
    # Simple check: Zenn slugs must be >= 12 chars.
    if len(slug) < 12:
        slug = f"{slug}-cozy-corner"
    return slug

def transform_post(file_path, filename):
    with open(file_path, 'r', encoding='utf-8') as f:
        # python-frontmatter automatically detects YAML (---) or TOML (+++)
        post = frontmatter.load(f)

    # 1. Map Hugo metadata to Zenn metadata
    zenn_metadata = {
        # Zenn requires specific fields
        'title': post.get('title', 'No Title'),
        'emoji': post.get('emoji', '🤖'), # Default emoji if missing
        'type': post.get('type', 'tech'), # 'tech' or 'idea'
        'topics': post.get('tags', [])[:5], # Zenn allows max 5 topics
        'published': not post.get('draft', False), # Invert Draft status
    }

    # 2. Prepare the content
    # You might want to remove Hugo specific shortcodes if Zenn doesn't support them
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

    # 3. Write to Zenn directory
    slug = zenn_slugify(filename)
    dest_path = os.path.join(DEST_DIR, f"{slug}.md")
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        yaml.dump(zenn_metadata, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n")
        f.write(f"![cover]({GITHUB_PAGES_BASE}/{post['cover']})\n" if pos
t.get('cover') else "\n")
        f.write(content)
    
    print(f"✅ Synced: {filename} -> {slug}.md")

def main():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.md'):
            transform_post(os.path.join(SOURCE_DIR, filename), filename)

if __name__ == "__main__":
    main()
