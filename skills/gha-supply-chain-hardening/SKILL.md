---
name: gha-supply-chain-hardening
description: Use to harden GitHub Actions and CMake dependencies across many repos: pin actions to commit SHAs, default read-only token, pin FetchContent to commits, verify with scans, optional attestations.
---

# GitHub Actions and CMake supply chain hardening

Companion to `plugin-ship-checklist` and `github-repo-lockdown`. Labels: MEASURED (done across 46 plugin repos), VERIFIED (source page), UNVERIFIED.

## The four changes, in order of value
1. Pin every action to a full commit SHA and keep the version in a comment: `uses: actions/checkout@<sha> # v4`. SHA pinning is the mainstream defence after the tj-actions compromise. VERIFIED (Semgrep blog, 2026). A SHA can still point at a commit in a malicious fork, so pinning is not a full answer. VERIFIED (platformengineering.org).
2. Top level `permissions: contents: read` in every workflow, widen per job only (release upload needs `contents: write`). Never use `pull_request_target` with a checkout of fork code. Background knowledge, UNVERIFIED.
3. Pin CMake `FetchContent_Declare(... GIT_TAG <full commit sha>)`. A branch name like `main` means any push to that repo changes your builds. CMake 3.28 accepted a commit SHA together with `GIT_SHALLOW ON`. MEASURED.
4. Publish SHA256SUMS with every release. UNVERIFIED as practice, cheap.

## Getting the SHA
`git ls-remote https://github.com/actions/checkout refs/tags/v4 refs/tags/v4^{}`. For a lightweight tag only one line prints and that SHA is the commit. For an annotated tag use the `^{}` line. MEASURED for checkout, upload-artifact, download-artifact, cache, setup-python.

## Rewriting many repos safely
- Script the edit with `sed -E` anchored on `@v4` followed by space or end of line, so `@v4.1` is not touched. Insert the permissions block before the first `^jobs:` only when no top-level `permissions:` exists. Parse every workflow with a YAML loader after editing. MEASURED.
- Work from a fresh `git fetch --depth=1` plus `reset --hard FETCH_HEAD` for each repo, never a stale clone: another session may have pushed. A stale clone gave a non-fast-forward rejection. MEASURED.
- Check workflows for write needs first: grep for `gh release`, `action-gh-release`, `git push`, `GITHUB_TOKEN`, `secrets.`. Only those need a wider job-level block. MEASURED.
- Verify at the end: no `uses:` line without a 40 hex SHA, no workflow without top-level `permissions:`, no `GIT_TAG main`. MEASURED.

## After pinning
- Dependabot security alerts do not see SHA pins, so keep the `# vX` comment and enable Dependabot version updates for the `github-actions` ecosystem, which rewrites pins. The version updates part is UNVERIFIED.
- Build provenance: `actions/attest-build-provenance` needs `id-token: write` and `attestations: write`; users check with `gh attestation verify FILE -R owner/repo`. Attestations alone give SLSA build level 2. VERIFIED (GitHub docs).
- GitHub org policy can block unpinned actions. VERIFIED (GitHub changelog 2025-08-15). Not available to personal accounts: UNVERIFIED.
