import os
from sync_utils import load_hugo_post, transform_image_urls, save_post, GITHUB_PAGES_BASE

SOURCE_DIR = 'content/en/posts'
DEST_DIR = 'devto_dist/posts'

def run_devto_sync():
    with os.scandir(SOURCE_DIR) as entries:
        for entry in entries:
            if not entry.is_file() or not entry.name.endswith('.md'):
                continue

            post = load_hugo_post(entry.path)
            slug = post.metadata.get('url', entry.name.replace('.md', '')).strip('/')

            metadata = {
                'title': post.get('title', 'No Title'),
                'description': post.get('description', ''),
                'tags': post.get('tags', []),
                'cover_image': post.get('cover', ''),
                'published': not post.get('draft', False),
                'canonical_url': f"{GITHUB_PAGES_BASE}/posts/{slug}/"
            }

            content = transform_image_urls(post.content)
            save_post(os.path.join(DEST_DIR, entry.name), metadata, content)
            print(f"✅ DEV.to: {entry.name}")

if __name__ == "__main__":
    run_devto_sync()
