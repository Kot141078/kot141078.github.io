# Article 50 Transparency Implementation Briefs v0.1

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgique  
**Year:** 2026  
**Status:** Supporting implementation briefs / technical notes  
**Boundary:** Not legal advice. Not certification. Not a conformity assessment. Not a formal Article 50 compliance claim. Formal compliance remains deployment-specific and subject to legal review.

## Purpose

This package contains two short implementation briefs derived from the Article 50 Transparency Submission Pack v0.1.

The purpose is to provide compact entry points for two audiences:

1. **AI Office / policy readers** - Article 50 transparency as an evidence chain:
   system boundary -> actor role -> obligation trigger -> disclosure or marking control -> evidence artifact -> responsible actor -> correction or review route.

2. **Engineers** - CGAM / witness / oracle degradation / human gate / rollback:
   task contract -> permission scope -> sandbox or worktree boundary -> witness event -> provenance sidecar -> human review -> release manifest -> rollback or correction route.

## Files

| File | Description |
|---|---|
| `01_For_AI_Office_Policy_Reader.md` | Short policy-reader note on Article 50 transparency as an evidence chain. |
| `01_For_AI_Office_Policy_Reader.pdf` | Academic PDF version of the policy-reader note. |
| `02_For_Engineers_CGAM_Witness_Oracle_Degradation.md` | Short engineering note on CGAM, witness events, oracle degradation, human gates, and rollback. |
| `02_For_Engineers_CGAM_Witness_Oracle_Degradation.pdf` | Academic PDF version of the engineering note. |
| `PACKAGE_MANIFEST.json` | Machine-readable package manifest. |
| `SHA256SUMS` | SHA256 integrity manifest for package files. |

## Relation to the Article 50 submission

This package is a supporting implementation layer.

It does not replace, revise, or extend the original Article 50 Transparency Submission Pack v0.1 as a submitted consultation package.

Related DOI for the original Article 50 Transparency Submission Pack v0.1:

<https://doi.org/10.5281/zenodo.20315439>

## Non-claim boundary

This package does not claim:

1. legal advice;
2. certification;
3. conformity assessment;
4. formal Article 50 compliance;
5. EU endorsement;
6. that witness records replace user-facing disclosure;
7. that metadata alone is sufficient where visible disclosure is required;
8. that human review is meaningful without a responsible human or organisation.

## Core implementation pattern

```text
system boundary
-> actor role
-> obligation trigger
-> disclosure or marking control
-> provenance / witness / audit evidence
-> human review where relevant
-> responsible actor
-> correction or review route
```

## Engineering implementation pattern

```text
AI-assisted workflow
-> task contract
-> permission scope
-> sandbox / worktree boundary
-> action
-> witness event
-> provenance sidecar
-> human review
-> human gate
-> release / rejection
-> rollback / correction route
```

## Integrity

Verify package integrity with:

```bash
sha256sum -c SHA256SUMS
```

On Windows PowerShell, compute hashes with:

```powershell
Get-FileHash -Algorithm SHA256 <file>
```
