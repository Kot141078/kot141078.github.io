# Beacon Profile v0.1 — Publication Bridge

## Purpose

This directory is an additive metadata and discovery bridge. It does not alter or supersede the historical Beacon Profile v0.1 files. It exists because the DOI was published after the original repository placement. The historical bytes and historical SHA-256 manifest remain authoritative for the GitHub snapshot.

## Published identifier

- Published DOI: `10.5281/zenodo.18933553`
- DOI URL: <https://doi.org/10.5281/zenodo.18933553>
- Zenodo record URL: <https://zenodo.org/records/18933553>
- DOI role: unresolved pending authoritative relation metadata
- Concept DOI: unresolved; not guessed

## Historical source artifacts

| Artifact | SHA-256 | Living mirror (`main`) | Immutable snapshot |
| --- | --- | --- | --- |
| `protocols/beacon/Beacon_Profile_v0.1_EN.md` | `4e5061fc655ce384dcbf75843ff158a10c5e1f39e3c2bdf60e2a85ffed494de1` | [main](https://github.com/Kot141078/advanced-global-intelligence/blob/main/protocols/beacon/Beacon_Profile_v0.1_EN.md) | [historical commit](https://github.com/Kot141078/advanced-global-intelligence/blob/15695853223c798379538aad69dc573730e1ee96/protocols/beacon/Beacon_Profile_v0.1_EN.md) |
| `protocols/beacon/Beacon_Profile_v0.1_EN.pdf` | `d646934ea8657785741af57e422d9e044a0de407f2f9d5a6089f083a37b6eeb0` | [main](https://github.com/Kot141078/advanced-global-intelligence/blob/main/protocols/beacon/Beacon_Profile_v0.1_EN.pdf) | [historical commit](https://github.com/Kot141078/advanced-global-intelligence/blob/15695853223c798379538aad69dc573730e1ee96/protocols/beacon/Beacon_Profile_v0.1_EN.pdf) |
| `protocols/beacon/README.md` | `9bf3b577e38519b7d25eb7051667e7c7db89b302c2f7ef5a80179593ed99dd26` | [main](https://github.com/Kot141078/advanced-global-intelligence/blob/main/protocols/beacon/README.md) | [historical commit](https://github.com/Kot141078/advanced-global-intelligence/blob/15695853223c798379538aad69dc573730e1ee96/protocols/beacon/README.md) |
| `hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt` | — | [main](https://github.com/Kot141078/advanced-global-intelligence/blob/main/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt) | [historical commit](https://github.com/Kot141078/advanced-global-intelligence/blob/15695853223c798379538aad69dc573730e1ee96/hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt) |

The Zenodo file inventory has not yet been ingested into this repository. Exact Zenodo ↔ GitHub byte identity is not claimed by this bridge.

## Status

Published DOI-linked informative synthesis profile containing normative-style local requirements. It is not a standards-track specification, not a certification regime, and not a completed cryptographic conformance package.

MUST / SHOULD language expresses the profile’s local design requirements but does not by itself establish independent interoperability.

## Public implementation evidence

- [Implementation module](https://github.com/Kot141078/ester-clean-code/blob/54cd0c8754587f5e9daf82b16eb84c66a7ac94ef/modules/beacon_profile/profile.py)
- [Implementation tests](https://github.com/Kot141078/ester-clean-code/blob/54cd0c8754587f5e9daf82b16eb84c66a7ac94ef/tests/test_beacon_profile.py)

Implementation status: Structural reference classifier and persistence sidecar.

The implementation currently demonstrates:

- Beacon bundle data structures;
- Slot A / Slot B classification flow;
- fail-closed downgrade;
- class-to-privilege mapping;
- local persistence of bundles and decisions;
- default rejection of raw-memory disclosure.

It does not currently demonstrate:

- recomputation of payload hashes;
- cryptographic signature verification;
- Ed25519 verification;
- key resolution;
- key rotation or revocation proof;
- witness-reference resolution;
- challenge execution;
- independent interoperability;
- production deployment conformance.

## Protocol boundary

- Beacon owns recognition semantics.
- VXCX owns bounded visual-experience capsule structure and transfer.
- L4 Witness owns challengeable evidence and consequence-bearing resolution.
- Valid VXCX evidence cannot independently raise Beacon class.
- Beacon recognition cannot independently prove VXCX content truth.
- Authority remains a separate local policy decision.

## Bridge discipline

- Explicit bridge coverage remains in section 16 of the [canonical profile](../Beacon_Profile_v0.1_EN.md).
- The two hidden bridges remain Ashby/requisite variety and bounded information-theoretic disclosure.
- Engineering/anatomical grounding remains in canonical section 17.
- This sidecar adds publication and implementation boundaries only.

## Citation

Kotov, Ivan. *Beacon Profile v0.1 — Inter-Entity Recognition for Sovereign Digital Entities*. v0.1, document dated 2026-03-09. Published DOI: <https://doi.org/10.5281/zenodo.18933553>.

## Non-claims

- No proof of consciousness, sentience, or personhood.
- No legal identity or civil status.
- No universal identity oracle.
- No provider-independent deployment certificate.
- No cryptographic conformance claim.
- No claim that API-key possession equals entity identity.
- No claim that access authority equals continuity identity.
