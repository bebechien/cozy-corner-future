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
- The site is built using `hugo --minify` and deployed to the `gh-pages` environment.

## 📂 Project Structure

- `assets/`: Media data for posts and pages.
- `content/`: Markdown content for posts and pages (organized by language).
- `themes/`: Contains the `terminal` theme submodule.
- `hugo.toml`: Main configuration file.
- `.github/workflows/`: CI/CD configuration for deployment.
