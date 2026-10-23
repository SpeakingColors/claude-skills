---
name: squarespace-expert
description: Use when planning, restyling or editing a Squarespace 7.1 site, covering pages, shop, hidden pages, code snippets, SEO, privacy and backups.
---

# Squarespace 7.1 Expert

Verify against current Squarespace pages before acting on anything marked UNVERIFIED; plan features change.
Assume the reader is not a programmer: give small, concrete steps, label what is unverified, and say plainly when something needs a higher plan.

## 0. Situation
- Typical target: a Squarespace version 7.1 site on an entry commerce plan (Basic), billed monthly or yearly. Confirm the reader's actual version and plan first (Settings > Billing, or ask).
- Check whether a Squarespace connector is available in the current session. If not, work by: a browser (built-in browser pane or a browser extension, using the reader's own sign-in), exported files the reader shares, and code/CSS/copy the reader pastes.
- Ask the reader for goals before changing anything: for example a portfolio-style site, a shop (print-on-demand or own products), pages to hide but keep, later audio links, downloads or demos.
- Ask for brand tokens (colors, fonts, logo) and mood (for example dark with accent colors) before restyling.
- Privacy rule worth proposing: no real address, phone, or personal details anywhere on the site, footer, policies, or image metadata unless the reader wants them public.

## 1. Squarespace 7.1 basics
- Fluid Engine is the 7.1 editor: free-placement blocks on a background grid inside sections (press G to show the grid). Classic sections upgraded to Fluid Engine cannot be reverted after saving; duplicate the section first.
- Structure: Pages hold Sections; Sections hold Blocks. Site-wide look lives in Website > Styles (fonts, colors, buttons, animations). Section-level color themes override per section.
- Mobile layout is set per section in Fluid Engine; always check it (see checklist).
- Collections: store, blog, portfolio, events, video, course pages hold items. Disabling or password-protecting a collection page also affects its items.
- Page states (Pages panel > gear):
  1. Enabled: live, indexable.
  2. Disabled: hidden from visitors and search engines, still editable by the site owner.
  3. Not linked: live at its URL but out of navigation (anyone with the URL can see it, search engines can index it unless noindex is set).
  4. Password protected: shared single password (max 30 chars, case-sensitive, 4-hour sessions, not per-person). Set it before adding content so it is not indexed.
- Site-wide password blocks checkout, so never use it on a live shop.
- Portfolio pages: up to 60 projects per page (duplicating help article).
- Duplicate Page copies layout and blocks into Not linked as "(Copy)", slug like /about-1. Page-specific header/footer content does not carry over.

## 2. Plan facts (official pricing and help pages, checked 2026-10-21)
Plans: Basic, Core, Plus, Advanced. VERIFIED (public pricing page): USD annual-billing prices are 19, 29, 49, 99 per month respectively. Prices in other currencies, monthly billing, discounts and taxes differ: check the pricing page for the reader's region.

| Feature | Basic | Core | Plus | Advanced |
|---|---|---|---|---|
| Store transaction fee | 2% | 0% | 0% | 0% |
| Digital content and memberships fee | 7% | 5% | 1% | 0% |
| Card rate (Squarespace Payments) | 2.9%+$0.30 | 2.9%+$0.30 | 2.7%+$0.30 | 2.5%+$0.30 |
| Custom CSS editor | Yes | Yes | Yes | Yes |
| Code block: HTML, Markdown, CSS in style tags | Yes | Yes | Yes | Yes |
| Code block: JavaScript, iframes | No | Yes | Yes | Yes |
| Code injection (site and per page) | No | Yes | Yes | Yes |
| Commerce APIs (API access) | No | Yes | Yes | Yes |
| Digital products, subscriptions, customer accounts | Yes | Yes | Yes | Yes |
| Payment plans, discounts | No | Yes | Yes | Yes |
| Contributors | 2 | Unlimited | Unlimited | Unlimited |
| Video storage | 30 min | 5 h | 50 h | Unlimited |

What this means on Basic:
1. CSS: allowed through the Custom CSS editor. Squarespace only supports it for fonts, colors, backgrounds; other CSS is at the site owner's own risk and unsupported.
2. Embed blocks are available on all plans, so many third-party widgets (donation buttons, audio players via embed URL) can work without JavaScript blocks. Which embeds work: test each; UNVERIFIED per widget.
3. No code injection, so no custom site-wide scripts, no tracking pixels via injection, no JS-based tweaks. Do not promise JS features on Basic.
4. No Commerce APIs on Basic, so no API-key scripts for products or orders. Printful and Printify still work (see section 3), probably through Squarespace's connection flow rather than customer API keys; mechanism UNVERIFIED.
5. 2% store fee on top of payment processing. Upgrading to Core removes the 2% fee and unlocks code injection and JS; weigh against volume. Upgrade does not need a new site.
6. Developer Platform / Developer Mode: the help article says Developer Platform is for version 7.0 on Core, Plus, Advanced only. Treat Developer Mode as NOT available for a 7.1 site. Turning it on in 7.0 blocks the update to 7.1.
7. Member areas: Member Sites exist in 7.1 (pages behind a paywall, free or paid, no page passwords inside them, no dropdown navigation). The help page states a website plan is needed to sell memberships; Basic carries a 7% digital content fee. Whether Basic can create member sites at all: UNVERIFIED.
8. Digital products (downloads) are included on Basic with the 7% fee. Good for sound banks or other files if sold; free downloads are better linked from a free host such as GitHub.
9. Pages: up to 1,000 on Basic. Keep pages under 5 MB and about 60 blocks.
Developer docs (developers.squarespace.com) describe Commerce APIs (Products, Orders, Inventory, Transactions, Webhooks) and a Custom Code spec for 7.1; plan limits there were not stated, rely on the pricing page.

## 3. Merch with Printful or Printify
Both need a store page in Squarespace first (Pages > + > Products under Sell), then connect from their dashboard (Printful: Stores > Choose platform > Squarespace; Printify: Manage my stores > Connect > Squarespace), approve in Squarespace, then publish products to the store page.
- Printful lists Basic, Core, Plus, Advanced (and legacy plans) as supported; Personal is not. Printify's page lists legacy plans and says new Core/Plus/Advanced "may also work"; Basic support in Printify's text is UNVERIFIED, test before committing.
- Neither article lists product or order limits. Squarespace 7.1 limits: 10,000 products, 250 variants each.
- Shipping: Squarespace shipping profiles apply to regions, not single products. Both vendors suggest flat rate, free shipping (price padded), or weight-based. Steps: Settings > Selling > Shipping (Printify) or Commerce > Shipping (Printful); copy the vendor's first-item and additional-item rates; for Printify per-order fee = first-item minus additional-item. Test by adding to cart logged out.
- Tax: Squarespace tax settings are separate. Printify may charge sales tax on US orders (resale certificate avoids it), VAT for EU/UK/Norway, local tax for items printed and shipped within Canada. Printful's Squarespace article says nothing on tax. The reader should confirm their own sales tax or VAT obligations with an accountant; UNVERIFIED here.
- Mockups: created in the Printful or Printify design tools. Generate several, keep images under 500 KB and 1500 to 2500 px wide, consistent backgrounds so the shop grid looks uniform. Edit titles, descriptions and prices in the vendor tool first; changes sync to Squarespace.
- Customer data: orders send the buyer's name and shipping address to the vendor for fulfilment. Which party is controller or processor: UNVERIFIED (Printful's privacy page text could not be read, and Printify's article is silent). Link the vendor privacy policies and write the site's own policy page; do not copy real personal details into it.
- Do not edit synced product fields in Squarespace if the vendor tool owns them; changes may be overwritten. UNVERIFIED, test on one product.

## 4. Working with Claude
What to export or share:
1. Screenshots of Pages panel, Website > Styles, and each page in desktop and mobile view.
2. Products CSV: Products panel > Export all (physical and service products only, up to 10,000; excludes images, alt text, reviews).
3. Site content XML: Settings > Import & export content > Export > WordPress. It covers layout pages, one blog, text and image blocks only. It excludes store pages, product and video blocks, drafts, styles, custom CSS, dropdowns. It cannot be re-imported into Squarespace. It is not a real backup.
4. A copy of the current Custom CSS (paste into a file) and a list of installed embeds.
5. Brand tokens: background and accent hex colors, fonts, logo files without personal metadata.

Backups and limits:
- Squarespace has no full site backup or one-click restore. Keep: Custom CSS text, the CSV, the XML, original images, page copy in Markdown, screenshots.
- "Duplicating a site" (separate help article, not read) can copy a whole site into a new one; billing and limits UNVERIFIED.

Driving the editor in a browser safely:
1. Use a new tab; ask the reader to be signed in. Never type or handle passwords, 2FA codes, or payment/card details; stop and hand over for billing, domain purchase, or Payments setup.
2. Work only in hidden or duplicated pages. Confirm with the reader before clicking Save/Publish on a live page, deleting anything, changing navigation, changing domain/DNS, or connecting apps.
3. Read before write: capture the current state (text and screenshot) so changes can be reverted by hand.
4. Prefer small, labeled steps; report each change made.
5. Squarespace editor autosaves drafts but live pages change only on Save; still treat every Save as publishing.

Staging workflow (no true staging site on Basic):
1. Duplicate the page (gear > Duplicate Page); the copy lands in Not linked.
2. Disable it or add a page password so it is private and not indexed, then build the new design.
3. Preview in desktop, tablet, mobile; test in incognito (custom code may not show while logged in).
4. When approved: swap content or navigation, set old page to Disabled (keep it for rollback), update slug and add a redirect if the URL changed.
5. To hide pages you want to keep (for example service pages): set Disabled (not deleted) or password-protected and Not linked. Restyling them in place first means the Styles and CSS changes carry over when they return. Disabled pages are invisible to search engines; Not linked pages are not.

Design approach for a dark look with accent colors:
- Set colors in Website > Styles > Colors (dark color as the Darkest/Dark theme, accent colors as Accent), and section themes per section. Use CSS only for extras (glow on buttons, hover effects, fonts).
- Keep contrast readable: bright accent text only on dark backgrounds, body text off-white.
- Give Claude CSS to paste into Design > Custom CSS; test in incognito.

SEO and domain:
1. Site title under 60 characters, site and page descriptions 50 to 300 characters, descriptive slugs, alt text on every image.
2. Connect the custom domain as the primary domain; set SSL to Secure (SEO checklist). Registrar and DNS steps: not researched, UNVERIFIED.
3. Verify in Google Search Console and Bing Webmaster Tools after publishing; the SEO Report tool finds missing alt text and descriptions.
4. Domain WHOIS privacy: UNVERIFIED for any given domain; check it so no home address is public.

Analytics, privacy, cookies:
- Built-in Squarespace Analytics needs no code. GA4 is connected with a G- measurement ID in the External API keys panel; this is a field, not code injection (plan requirement not stated).
- Cookie banner: Cookies & Data Privacy panel > Cookie banner on; choose Decline all and Manage cookies buttons. Restricted cookies are not set until accepted. Needed when using analytics, embeds (YouTube, SoundCloud, donation widgets) or marketing cookies for visitors in regions with consent rules (EU/UK, Quebec). Exact legal duty: UNVERIFIED, not legal advice.
- Add a privacy policy and shipping/returns pages to the shop. Squarespace has sample policy text; edit it, leave out street address if the reader works from home.
- Analytics log: your own visits count while logged in.

## 5. Pitfalls
1. Not linked pages are still public by URL; use Disable or password for privacy.
2. Site-wide password breaks checkout.
3. Custom code is unsupported by Squarespace support; test in incognito and keep a copy of every snippet.
4. Fluid Engine mobile layouts often need separate tuning; text overlapping images on mobile is the common bug.
5. Changing a slug without a redirect breaks links, including links posted on social media, donation pages, GitHub READMEs.
6. Oversized images: keep under 500 KB, 1500 to 2500 px wide, sRGB, filenames with letters, numbers, hyphens only.
7. Too many embeds (audio, video) slow pages; keep under about 60 blocks and spread players across pages.
8. Uploaded files (PDFs, audio) uploaded before a page was password-protected may stay indexed; re-upload.
9. Image EXIF data can include location; strip metadata from photos before upload. Squarespace handling of EXIF: UNVERIFIED.
10. Basic plan fee: 2% store fee plus processing; digital products 7%. Price products with that in mind.
11. Audio: serving large audio files on Squarespace is limited by plan/storage; prefer embeds from Bandcamp, SoundCloud or GitHub release links. Plan limits for audio blocks: UNVERIFIED.
12. Renewal: check the billing date and term; downgrading or upgrading mid-term billing rules UNVERIFIED.

## 6. Pre-publish checklist
1. All text read; no placeholder text; site title set.
2. Privacy scan: search the site and exports for real name, address, phone, personal email, EXIF location, domain WHOIS; contact via a form or role email only.
3. Every link clicked: shop, donation pages, GitHub, social, downloads; no links to disabled or password pages.
4. Mobile and tablet view checked for every changed page; test on a real phone.
5. Page size under 5 MB (Chrome DevTools Network tab), images under 500 KB, alt text added.
6. Test order or checkout flow with a real small product, then cancel and refund; the reader handles any payment step themselves.
7. Shipping rates and tax checked with logged-out cart for the home country, one neighboring country, one other region.
8. Forms tested; cookie banner on; privacy and shipping policies linked in footer.
9. Hidden pages confirmed Disabled or protected and absent from navigation and sitemap.
10. Page descriptions, social sharing image, favicon set; Search Console verified after launch.
11. Backups saved: Custom CSS text, products CSV, XML export, screenshots.
12. The reader gives explicit go-ahead before Save/Publish.

## Sources (fetched)
- https://www.squarespace.com/pricing
- https://support.squarespace.com/hc/en-us/articles/206536797
- https://support.squarespace.com/hc/en-us/articles/205815928-Adding-custom-CSS-to-your-site
- https://support.squarespace.com/hc/en-us/articles/205815908
- https://support.squarespace.com/hc/en-us/articles/360038270572
- https://support.squarespace.com/hc/en-us/articles/6421525446541-Edit-your-site-with-Fluid-Engine
- https://support.squarespace.com/hc/en-us/articles/206543067-Enabling-and-disabling-pages
- https://support.squarespace.com/hc/en-us/articles/205814618-Page-passwords
- https://support.squarespace.com/hc/en-us/articles/205815528-Site-wide-passwords
- https://support.squarespace.com/hc/en-us/articles/206543627-Duplicating-pages-and-content
- https://support.squarespace.com/hc/en-us/articles/206566687-Exporting-your-site
- https://support.squarespace.com/hc/en-us/articles/360000694948-Export-products-to-a-csv
- https://support.squarespace.com/hc/en-us/articles/206545727-Providing-cookie-consent-options-with-a-banner
- https://support.squarespace.com/hc/en-us/articles/205815608-Connect-Google-Analytics-to-your-site
- https://support.squarespace.com/hc/en-us/articles/360002090267-SEO-checklist
- https://support.squarespace.com/hc/en-us/articles/360022518252-Site-launch-checklist
- https://support.squarespace.com/hc/en-us/articles/206542517-Formatting-images-for-display-on-the-web
- https://support.squarespace.com/hc/en-us/articles/360022529371-Reducing-your-page-size-for-faster-loading
- https://support.squarespace.com/hc/en-us/articles/360050832631-Member-Sites
- https://developers.squarespace.com/
- https://developers.squarespace.com/commerce-apis/overview
- https://help.printful.com/hc/en-us/articles/360014009180-How-do-I-connect-Squarespace-with-Printful
- https://help.printful.com/hc/en-us/articles/360014009200-Which-Squarespace-plan-do-I-need-to-integrate-with-Printful
- https://help.printful.com/hc/en-us/articles/360014009220-How-do-I-configure-shipping-for-Squarespace
- https://help.printify.com/hc/en-us/articles/4483616002961-How-can-I-connect-my-Squarespace-store
- https://help.printify.com/hc/en-us/articles/4483623895825-How-do-I-set-up-shipping-with-Squarespace
- https://help.printify.com/hc/en-us/articles/4483644252433-Which-taxes-apply-when-I-use-Printful
- https://www.printful.com/policies/privacy (fetched, text not readable)
