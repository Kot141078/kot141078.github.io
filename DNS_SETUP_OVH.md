# DNS setup in OVH

## Apex domain `ivankotov.eu`

- `A 185.199.108.153`
- `A 185.199.109.153`
- `A 185.199.110.153`
- `A 185.199.111.153`

## `www`

- `CNAME -> kot141078.github.io`

## Note

- custom domain already set to `ivankotov.eu`
- after DNS propagation, enable Enforce HTTPS

## Secondary domain

- `advancedglobalintelligence.eu`
- manual `301` redirect to:
  `https://ivankotov.eu/advanced-global-intelligence/`
