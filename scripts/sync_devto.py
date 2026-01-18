import os
from sync_utils import load_hugo_post, transform_image_urls, save_post, GITHUB_PAGES_BASE

SOURCE_DIR = 'content/en/posts'
DEST_DIR = 'devto_dist/posts'

def run_devto_sync():
    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith('.md'): continue

        post = load_hugo_post(os.path.join(SOURCE_DIR, filename))
        slug = post.metadata.get('url', filename.replace('.md', '')).strip('/')
        
        metadata = {
            'title': post.get('title', 'No Title'),
            'description': post.get('description', ''),
            'tags': post.get('tags', []),
            'cover_image': post.get('cover', ''),
            'published': not post.get('draft', False),
            'canonical_url': f"{GITHUB_PAGES_BASE}/posts/{slug}/"
        }

        content = transform_image_urls(post.content)
        save_post(os.path.join(DEST_DIR, filename), metadata, content)
        print(f"✅ DEV.to: {filename}")

if __name__ == "__main__":
    run_devto_sync()