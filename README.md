# S&S Legal website

The website for S&S Legal, Barristers & Solicitors, F233/2 Wentum Street, Osu, Accra.

A static site: plain HTML, CSS and JavaScript, with no database or WordPress. It loads quickly, is cheap or free to host, and has very little to keep patched. It includes a light and a dark theme, follows each visitor's device setting, and has a switch in the header.

## Pages

| Page | File |
|---|---|
| Home | `index.html` |
| Expertise overview | `expertise/index.html` |
| Business · Disputes · Private clients | `expertise/business/`, `expertise/disputes/`, `expertise/private-clients/` |
| Our lawyers | `lawyers/index.html` |
| Lawyer profiles (5) | `lawyers/<name>/index.html` |
| About | `about/index.html` |
| Contact | `contact/index.html` |
| Privacy notice | `privacy/index.html` |
| Page not found | `404.html` |

Also: `sitemap.xml`, `robots.txt`, structured data so search engines can show the firm's address, phones and hours, and sharing previews for each page.

## Editing content

All wording, lawyers, practice areas and contact details live in **`build.py`**. Do not edit the `.html` files by hand: they are generated.

1. Edit `build.py`, for example the `FIRM`, `PEOPLE`, `GROUPS` or `AREAS` sections.
2. Rebuild the pages:

   ```bash
   python3 build.py
   ```

3. Check that every link, anchor and image still resolves:

   ```bash
   python3 tools/check_links.py
   ```

4. Commit and push.

Styles are in `assets/css/styles.css`. Colours are defined once at the top, for the light theme and again for the dark theme. Behaviour (menu, theme switch, copy buttons, the form) is in `assets/js/site.js`. Photos and the logo are in `assets/img/`.

## Publishing

### GitHub Pages
1. In the repository on GitHub: **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. The site appears at `https://<account>.github.io/<repository>/` within a minute or two.

To serve it at **sslegal.org**, add the domain under **Settings → Pages → Custom domain**. Then point the domain's DNS at GitHub Pages, as GitHub's instructions describe. Only do this once the firm is ready to retire the current WordPress site.

### Netlify or similar
Drag the folder into Netlify, or connect the repository. There is no build command, and the publish directory is the repository root.

## The consultation form

With no form service set up, the form opens the visitor's email app with their request filled in and addressed to info@sslegal.org. To receive requests directly instead:

1. Create a form endpoint with a service such as Formspree or Netlify Forms.
2. In `build.py`, find `consult_form` and add `data-endpoint="https://…your endpoint…"` to the `<form>` tag.
3. Rebuild.

## Before launch

- [ ] **Logo:** replace `assets/img/sslegal-logo.png` (82 px) with the original vector logo, or a large PNG of at least 400 px.
- [ ] **Photos:** replace the portraits in `assets/img/` with the original high-resolution files. Keep the same file names.
- [ ] **Profiles to confirm:**
  - Bassing Ali Kamaldeen: LL.B. institution and LL.M. status.
  - Dr Abdul Razak Sania: title and Ghana Bar Association membership while in professional training.
  - Nana Akwasi Asafo-Adjei: the Cornell fellowship listed on the current website (left out here).
- [ ] **WhatsApp:** confirm which number receives WhatsApp messages. It is currently +233 24 447 6615, set in `FIRM['whatsapp']`.
- [ ] **Wording:** approve the new opening line, practice summaries, the "Working with us" steps and the privacy notice.
- [ ] **Form:** decide between the email hand-off and a form service (see above).
- [ ] **Current site:** until the switch, unpublish the WordPress theme's demo pages (Shop, Cart, Checkout, Pricing Tables, Sample Page and others), and update the © 2017 footer and the broken Twitter link.

Content is taken from the firm's current website at sslegal.org, lightly edited for clarity and in keeping with the profession's rules on advertising.
