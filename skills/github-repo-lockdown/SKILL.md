---
name: github-repo-lockdown
description: Use when public GitHub repos must be fork-only: strangers can read, fork and download releases but not push, open issues, comment or open PRs. gh commands, limits, renewal workflow, pitfalls.
---

# GitHub repo lockdown: read, fork, download, nothing else

Companion to `github-expert` and `github-for-beginners`. Labels: MEASURED (done on 66 real repos in one session), VERIFIED (read on a source page), UNVERIFIED (believed, test first).

## What strangers can still do, and what you can switch off
- Forking a public repo cannot be turned off. UNVERIFIED here, believed from GitHub docs. That is the intended "fork it and make it yours" path.
- Pushing is already impossible for people who are not collaborators. Never add collaborators you do not want.
- Switch off the rest per repo: issues, wiki, projects, discussions, and pull request creation.

## Commands (run on your own computer where `gh auth login` is done with your account)
Cloud coding sessions cannot do this: the session proxy answered `Repository settings writes are not permitted through this proxy` (HTTP 403). MEASURED. A GitHub token cannot be saved for api.github.com in such a session either.
1. Test on ONE repo first:
```bash
R=OWNER/REPO
gh api -X PATCH repos/$R -f pull_request_creation_policy=collaborators_only --jq .pull_request_creation_policy   # prints collaborators_only
gh api -X PUT repos/$R/actions/permissions/fork-pr-contributor-approval -f approval_policy=all_external_contributors && echo ok
gh api -X PUT repos/$R/branches/main/protection --input - <<'EOF2'
{"required_status_checks":null,"enforce_admins":false,"required_pull_request_reviews":null,"restrictions":null,"allow_force_pushes":false,"allow_deletions":false}
EOF2
```
All three worked on public repos. MEASURED.
2. Then every repo: `gh repo list OWNER --source --no-archived -L 200 --json name --jq '.[].name'` in a `for` loop, with `gh api -X PATCH repos/OWNER/$R -F has_issues=false -F has_wiki=false -F has_projects=false -F has_discussions=false`.
3. Check without a token: `curl -s https://api.github.com/repos/OWNER/REPO` and read `has_issues`, `pull_request_creation_policy`. MEASURED.

## Known errors, all harmless
- Private repos: `Fork PR approval is not allowed for private repositories`, and branch protection says `Upgrade to GitHub Pro` on a free plan. Private repos cannot be forked by strangers anyway. MEASURED.
- macOS `base64` has no `-w0`. Use `base64 -i file | tr -d '\n'`. An upload with a blank `content` creates an EMPTY file and succeeds silently; fix it with a PUT that passes the file's current `sha`. MEASURED.
- A `PUT contents` on an existing file without `sha` fails with 422, and with a stale `sha` with 409. MEASURED.

## Comments on commits and the six month limit
- Interaction limits: `gh api -X PUT repos/OWNER/REPO/interaction-limits -f limit=collaborators_only -f expiry=six_months`. Six months is the longest expiry, so it must be renewed. Whether it also covers comments on commits is UNVERIFIED.
- Renew automatically on GitHub: a scheduled workflow in a repo you own, using a secret `LOCK_TOKEN` (classic token, `repo` scope, no expiration; create at github.com/settings/tokens/new, store with `gh secret set LOCK_TOKEN --repo OWNER/.github`). The default `GITHUB_TOKEN` cannot change repo settings. MEASURED (the run was started; it loops over every public repo).
- GitHub disables scheduled workflows in public repos after 60 days without repo activity. A final step that calls `PUT /repos/{repo}/actions/workflows/{file}/enable` is meant to prevent that. UNVERIFIED, check Actions after about two months.

## Message to outsiders
- Put a short `CONTRIBUTING.md` in the account's `.github` repo (default for every repo without its own). Say: forks welcome, no outside contributions, provided as is. Do not promise a security contact you do not want. Repos whose name starts with a dot cannot be attached to cloud coding sessions, so edit that one with `gh api -X PUT repos/OWNER/.github/contents/CONTRIBUTING.md`. MEASURED.
- Private vulnerability reporting is optional and invites mail. Leave it off if you do not want to deal with reports.
