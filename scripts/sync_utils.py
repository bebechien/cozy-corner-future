import os
import re
import frontmatter
import yaml

def get_base_url():
    """Extracts baseURL from hugo.toml."""
    try:
        with open('hugo.toml', 'r', encoding='utf-8') as f:
            content = f.read()
            # Supports baseURL = "url", baseURL = 'url', baseURL=url
            match = re.search(r'baseURL\s*=\s*["\']?(.*?)["\']?\s*(?:#.*)?$', content, re.MULTILINE)
            if match:
                return match.group(1).strip().rstrip('/')
    except FileNotFoundError:
        pass
    return "https://bebechien.github.io/cozy-corner-future"

GITHUB_PAGES_BASE = get_base_url()

def load_hugo_post(file_path):
    """Loads a Hugo markdown file and returns a post object."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return frontmatter.load(f)

def transform_image_urls(content, base_url=GITHUB_PAGES_BASE):
    """Converts local image paths ![alt](/path.png) to absolute URLs."""
    def image_replacer(match):
        alt_text, img_path = match.groups()
        if img_path.startswith('http'):
            return match.group(0)
        
        clean_path = img_path.lstrip('/')
        return f'![{alt_text}]({base_url}/{clean_path})'

    # Matches ![alt](path)
    return re.sub(r'!\[(.*?)\]\((.*?)\)', image_replacer, content)

def save_post(dest_path, metadata, content):
    """Writes the transformed post with new YAML frontmatter."""
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        yaml.dump(metadata, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n")
        f.write(content)