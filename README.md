# Cozy Corner Future

This is the source code for the **[Cozy Corner Future](https://bebechien.github.io/cozy-corner-future/)** website, built with [Hugo](https://gohugo.io/) and hosted on GitHub Pages.

## 🌍 Multilingual Support

The site is available in the following languages:
- **English** (Default)
- **Korean** (한국어)
- **Japanese** (日本語)

## 🎨 Theme

This site uses the [Terminal](https://github.com/panr/hugo-theme-terminal) theme.

## 🚀 Getting Started

### Prerequisites

- [Hugo](https://gohugo.io/getting-started/installing/) (Extended version recommended)
- Git

### Local Development

1.  **Clone the repository:**

    ```bash
    git clone --recurse-submodules https://github.com/bebechien/cozy-corner-future.git
    cd cozy-corner-future
    ```

2.  **Run the Hugo server:**

    ```bash
    hugo server -D
    ```

3.  **Preview the site:**
    Open your browser and navigate to `http://localhost:1313/cozy-corner-future/`.

## 📦 Deployment

Deployment is handled automatically via **GitHub Actions**.

- Pushing to the `main` branch triggers the [Deploy to GitHub Pages](.github/workflows/deploy.yaml) workflow.
- The site is built using `hugo --minify` and deployed to the `gh-pages` branch.

## ✍️ Zenn Integration

This repository automatically syncs Japanese content to [Zenn](https://zenn.dev/).

### How it works

1.  **Source of Truth:** Japanese posts are written in `content/ja/posts/`.
2.  **Transformation:** The `scripts/sync_zenn.py` script converts Hugo Markdown files into Zenn-compatible format (mapping frontmatter, handling slugs, etc.).
3.  **Automation:** The [Zenn Sync](.github/workflows/zenn-sync.yaml) workflow runs on pushes to `main`.
    - It executes the transformation script.
    - It prepares a Zenn-compatible directory structure (`zenn_dist`).
    - It deploys the content of `zenn_dist` to the `zenn-sync` branch.
    - You can connect your Zenn account to the `zenn-sync` branch of this repository.

### Zenn-specific Directories

- `articles/`: Destination for generated Zenn articles (used by the sync script).
- `books/`: Placeholder for Zenn books.
- `scripts/`: Contains the `sync_zenn.py` transformation script.

## 🦄 DEV.to Integration

This repository automatically syncs English content to [DEV.to](https://dev.to/).

### How it works

1.  **Source of Truth:** English posts are written in `content/en/posts/`.
2.  **Transformation:** The `scripts/sync_devto.py` script prepares the content (fixing image URLs to be absolute, mapping frontmatter).
3.  **Automation:** The [DEV.to Sync](.github/workflows/devto-sync.yaml) workflow runs on pushes to `main`.
    - It prepares the content in `devto_dist/`.
    - It pushes the prepared content to the `devto-sync` branch.
    - It uses the `sinedied/publish-devto` action to publish/update articles on DEV.to using the API.

## 📝 Velog Integration

For Korean content, a helper script is provided to prepare posts for [Velog](https://velog.io/).

### How it works

1.  **Source of Truth:** Korean posts are written in `content/ko/posts/`.
2.  **Preparation:** Run the script manually:
    ```bash
    python scripts/prepare_velog.py
    ```
3.  **Result:** The script generates Velog-ready Markdown files in `velog_dist/`.
    - Image paths are converted to absolute GitHub Pages URLs.
    - A canonical link footer is added.
    - Frontmatter is stripped (since Velog uses a UI for metadata).
4.  **Publishing:** Copy the content from the generated file and paste it into the Velog editor.

## 📂 Project Structure

- `assets/`: Media data for posts and pages.
- `content/`: Markdown content for posts and pages (organized by language).
- `scripts/`: Python scripts for content synchronization and transformation.
- `themes/`: Contains the `terminal` theme submodule.
- `hugo.toml`: Main configuration file.
- `.github/workflows/`: CI/CD configuration for deployment.
