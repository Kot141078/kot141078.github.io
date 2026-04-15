# REPORT_SITE_BOOTSTRAP

## What was done

- preflight checks passed in fail-closed mode
- new local repository created at `C:\Users\kotov\Desktop\AGI\kot141078.github.io`
- static site created as plain HTML + CSS
- files created:
  - `index.html`
  - `styles.css`
  - `404.html`
  - `CNAME`
  - `robots.txt`
  - `sitemap.xml`
  - `README.md`
  - `advanced-global-intelligence/index.html`
  - `c-a-plus-b/index.html`
  - `DNS_SETUP_OVH.md`
  - `REDIRECT_PLAN_ADVANCEDGLOBALINTELLIGENCE_EU.md`
  - `REPORT_SITE_BOOTSTRAP.md`
- remote repository created: `https://github.com/Kot141078/kot141078.github.io`
- `origin` bound to the local repository
- first commit created and pushed to `main`
- GitHub Pages observed as enabled from branch `main` path `/`
- custom domain observed as set to `ivankotov.eu`

## What was not done

- OVH DNS records were not changed from this environment
- `Enforce HTTPS` was not enabled because DNS resolution still needs to propagate
- `advancedglobalintelligence.eu` was not attached as a second custom domain to GitHub Pages

## Paths

- local path: `C:\Users\kotov\Desktop\AGI\kot141078.github.io`
- remote URL: `https://github.com/Kot141078/kot141078.github.io`

## Commit hashes

- bootstrap content commit: `41e0e6657b478b3f89c00a6794f662da593f0c7f`
- Pages build source commit: `41e0e6657b478b3f89c00a6794f662da593f0c7f`

## Pages status

- enabled
- source: branch `main`, path `/`
- last observed build status: `built`
- last observed site URL: `http://ivankotov.eu/`
- `custom_404`: `true`

## Custom domain status

- set
- domain: `ivankotov.eu`
- observed `https_enforced`: `false`

## OVH manual steps remaining

- for apex `ivankotov.eu`, create:
  - `A 185.199.108.153`
  - `A 185.199.109.153`
  - `A 185.199.110.153`
  - `A 185.199.111.153`
- for `www`, create:
  - `CNAME -> kot141078.github.io`
- for `advancedglobalintelligence.eu`, configure a manual permanent `301` redirect to:
  - `https://ivankotov.eu/advanced-global-intelligence/`
- after DNS propagation confirms the primary domain, enable `Enforce HTTPS` in GitHub Pages

## Existing repositories

- confirmed: no existing repository in `C:\Users\kotov\Desktop\AGI` was modified
