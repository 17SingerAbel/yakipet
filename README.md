# Yakipet catalog website

A lightweight, static B2B product catalog for [yakipet.com](https://yakipet.com). It uses only HTML and CSS, with no build step, backend, or dependencies.

## Make it yours

### Replace product photos

Each product has its own folder under `images/products/`. The catalog card uses that product's `cover-web.jpg`; the other photos in the folder are the original detail images.

To change a cover, add an optimized square image to the product folder and update the matching `src` path and `alt` text in `index.html`. Images around 1200 × 1200 px work well and should be compressed so the site stays fast. Keep the high-resolution originals if you need them for future product-detail pages, but avoid loading them directly on the homepage.

### Update products and prices

Open `index.html` and find the `product-grid` section. Each `<article class="product-card">` contains one product's image, name, description, price, and MOQ. Edit the text directly, duplicate a complete article to add a product, or remove one to delete a product.

### Update contact information

Open `index.html` and search for `Replace these placeholder details`. Replace the placeholder email and phone number in both the visible text and the `mailto:` / `tel:` links. The location is currently Ontario, Canada.

## Preview locally

Open `index.html` directly in a browser, or run a small local server from this folder:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploy with GitHub Pages

1. Create a GitHub repository and push all files in this folder to its `main` branch.
2. On GitHub, open **Settings → Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Choose the `main` branch and `/ (root)` folder, then click **Save**.
5. In your domain provider's DNS settings, point `yakipet.com` to GitHub Pages using GitHub's documented apex-domain records.
6. Back in **Settings → Pages**, confirm `yakipet.com` as the custom domain and enable **Enforce HTTPS** after DNS finishes updating.

The included `CNAME` file already contains `yakipet.com`. Keep it in the repository root.
