# ISH / ICH2026 frontend

Static one-page frontend designed for embedding in Google Sites through
`Insert > Embed > Embed URL`.

## Files

- `index.html`: page content and structure.
- `styles.css`: responsive design, layout, motion and theme.
- `script.js`: mobile menu, scroll reveal and active navigation state.

## Local preview

This can be opened directly in a browser:

`/mnt/data2/pagina_nicole/frontend/index.html`

For a closer production preview, serve the folder with any static server and open
the generated local URL.

## Hosting for Google Sites embed

Deploy this folder to a static host such as GitHub Pages, Netlify, Vercel,
Cloudflare Pages or Firebase Hosting. Then insert the public URL in Google Sites.

Important iframe requirement: the hosting service must not block embedding with
`X-Frame-Options` or a restrictive `Content-Security-Policy frame-ancestors`
header.

Target Google Site page:

`https://sites.google.com/view/jejetesting/p%C3%A1gina-principal`

After deployment:

1. Open the Google Sites editor for that page.
2. Choose `Insert > Embed`.
3. Select `By URL`.
4. Paste the deployed frontend URL.
5. Resize the embed block to full width and enough height for the page.
6. Preview desktop and mobile before publishing.

For a full-page effect in Google Sites, keep the Google Sites page itself almost
empty and place only this embed on it.

## Asset note

Current images are public URLs extracted from the reference site and should be
treated as placeholders unless you have permission to reuse them. Replace them
with authorized local files before final publication.
