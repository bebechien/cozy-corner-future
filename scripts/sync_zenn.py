import os
from sync_utils import load_hugo_post, transform_image_urls, save_post, GITHUB_PAGES_BASE

SOURCE_DIR = 'content/ja/posts'
DEST_DIR = 'zenn_dist/articles'

def zenn_slugify(filename):
    slug = os.path.splitext(filename)[0]
    return slug if len(slug) >= 12 else f"{slug}-cozy-corner"

def run_zenn_sync():
    with os.scandir(SOURCE_DIR) as entries:
        for entry in entries:
            if not entry.is_file() or not entry.name.endswith('.md'):
                continue

            post = load_hugo_post(entry.path)

            # Zenn specific mapping
            metadata = {
                'title': post.get('title', 'No Title'),
                'emoji': post.get('emoji', '🤖'),
                'type': post.get('type', 'tech'),
                'topics': post.get('tags', [])[:5],
                'published': not post.get('draft', False),
            }

            content = transform_image_urls(post.content)

            # Add cover image if exists
            if post.get('cover'):
                content = f"![cover]({GITHUB_PAGES_BASE}/{post['cover']})\n\n" + content

            save_post(os.path.join(DEST_DIR, f"{zenn_slugify(entry.name)}.md"), metadata, content)
            print(f"✅ Zenn: {entry.name}")

if __name__ == "__main__":
    run_zenn_sync()
