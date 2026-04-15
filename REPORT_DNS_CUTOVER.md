# REPORT_DNS_CUTOVER

- Date: `2026-04-15`
- Iteration ID: `SITE_DNS_CUTOVER_IVANKOTOV_EU_02`
- Result: `partial`
- Mode: `fail-closed`

## What was done

- preflight completed on `C:\Users\kotov\Desktop\AGI\kot141078.github.io`
- snapshot artifacts created under `artifacts/dns-cutover/`
- current GitHub Pages repo state captured
- current DNS and HTTP state captured for:
  - `ivankotov.eu`
  - `www.ivankotov.eu`
  - `advancedglobalintelligence.eu`
  - `www.advancedglobalintelligence.eu`
- partial-state report created without changing any repository except the site repository

## What was not done

- OVH DNS records were not changed
- OVH redirect configuration was not changed
- GitHub profile-level domain verification for `ivankotov.eu` was not completed
- GitHub TXT verification record name/value was not obtained from the required profile Pages flow
- `Enforce HTTPS` was not enabled

## Blocker

This environment has no authenticated OVH control channel and no browser automation tool available for the OVH UI.

This environment also has no available GitHub profile Pages verified-domain control path:

- `gh auth status` is valid for repository access
- repository Pages API is reachable
- profile-level guessed API paths such as `user/pages` and `user/pages/verified-domains` return `404`
- no MCP/browser resource is available for interactive GitHub profile settings

Because the contract is `FAIL-CLOSED`, no DNS, verification, or redirect changes were guessed or simulated.

## Exact current state

### Apex A records

Observed current `A` answer for `ivankotov.eu`:

- `213.186.33.5`

Expected for GitHub Pages cutover:

- `185.199.108.153`
- `185.199.109.153`
- `185.199.110.153`
- `185.199.111.153`

Status:

- not cut over

### WWW CNAME

Observed current state for `www.ivankotov.eu`:

- no `CNAME` answer present
- current `A` answer observed separately: `213.186.33.5`

Expected:

- `CNAME -> kot141078.github.io`

Status:

- not cut over

### TXT verification

Observed current apex TXT answers for `ivankotov.eu`:

- `1|www.ivankotov.eu`
- `v=spf1 include:mx.ovh.com -all`

GitHub verification TXT:

- exact record name: not obtained
- exact record value: not obtained

GitHub verified domain status:

- `blocked`

### GitHub Pages custom domain status

Observed from repository Pages API:

- Pages enabled: `true`
- source branch: `main`
- source path: `/`
- custom domain: `ivankotov.eu`
- `https_enforced`: `false`

### HTTPS status

Observed HTTP/HTTPS behavior:

- `http://ivankotov.eu` -> `302 Moved Temporarily` to `http://www.ivankotov.eu`
- `https://ivankotov.eu` -> connection reset
- `http://www.ivankotov.eu` -> `200 OK` from OVH
- `https://www.ivankotov.eu` -> connection reset

Status:

- not ready for `Enforce HTTPS`

### Redirect status for `advancedglobalintelligence.eu`

Observed current behavior:

- `http://advancedglobalintelligence.eu` -> `302 Moved Temporarily` to `http://www.advancedglobalintelligence.eu`
- `http://www.advancedglobalintelligence.eu` -> `200 OK` from OVH
- `https://advancedglobalintelligence.eu` -> connection failed
- `https://www.advancedglobalintelligence.eu` -> connection failed

Expected target:

- `https://ivankotov.eu/advanced-global-intelligence/`

Required redirect mode:

- permanent `301`

Status:

- not configured as required

## Manual work remaining

- In OVH for `ivankotov.eu`, replace only conflicting root web-routing records so that apex resolves to:
  - `185.199.108.153`
  - `185.199.109.153`
  - `185.199.110.153`
  - `185.199.111.153`
- In OVH for `www.ivankotov.eu`, leave only:
  - `CNAME -> kot141078.github.io`
- Keep non-conflicting `NS`, `SOA`, `MX`, and mail-related TXT records intact.
- In GitHub profile settings for user `Kot141078`, open Pages verified domains, add `ivankotov.eu`, and copy the exact TXT host/value required by GitHub.
- In OVH, add that TXT record exactly as GitHub specifies and keep it after verification.
- After DNS propagation and successful certificate issuance, enable `Enforce HTTPS` in repository Pages settings.
- In OVH for `advancedglobalintelligence.eu`, configure a permanent `301` redirect to:
  - `https://ivankotov.eu/advanced-global-intelligence/`
- Do not connect `advancedglobalintelligence.eu` as a second GitHub Pages custom domain.

## Artifact path

- `C:\Users\kotov\Desktop\AGI\kot141078.github.io\artifacts\dns-cutover`

## Repository boundary

- confirmed: no repository outside `C:\Users\kotov\Desktop\AGI\kot141078.github.io` was modified
