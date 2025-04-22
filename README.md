# greatjobdave.net

Personal blog built with Jekyll, featuring music, code, and more.

## Development

### Prerequisites

- Ruby 3.2.2
- Bundler
- Jekyll

### Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/greatjobdave.git
cd greatjobdave
```

2. Install dependencies
```bash
bundle install
```

3. Run locally
```bash
bundle exec jekyll serve --drafts
```

The site will be available at `http://localhost:4000`

### Project Structure

```
.
├── _drafts/          # Draft posts
├── _posts/           # Published posts
├── _layouts/         # Layout templates
├── assets/
│   ├── css/         # Stylesheets
│   ├── images/      # Images and media
│   └── js/          # JavaScript files
├── _config.yml      # Site configuration
└── index.md         # Homepage
```

### Writing Posts

- Create new posts in `_drafts/` for drafts
- Move to `_posts/` with filename `YYYY-MM-DD-title.md` to publish
- Use front matter for post metadata:
  ```yaml
  ---
  layout: post
  title: "Post Title"
  date: YYYY-MM-DD
  categories: [category1, category2]
  ---
  ```

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `master` branch. 