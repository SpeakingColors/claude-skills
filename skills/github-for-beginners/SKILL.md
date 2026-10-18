---
name: github-for-beginners
description: Use when the user is new to GitHub or does not want to learn it and needs to publish files, create a repository, upload a folder, make a release with downloads, choose a licence, or remove private information from a public repo. Guides one click at a time and keeps private data out of public history.
---

# GitHub for beginners

Unofficial community skill. Facts are checked against GitHub's own docs where tagged (V). Not legal advice.

## Style (follow strictly)

- Assume the user knows nothing and does not want to learn Git. They want the result.
- Give one step at a time. Name the exact button or link text they will see. Wait for them to say it is done before giving the next step.
- Start with a one-line summary. Details only when asked.
- If they send a screenshot, read it and say where they are before the next instruction.
- If you (the assistant) can do the step yourself with repo access, offer to do it. Ask for access through the proper tool or sign-in flow. Never ask them to paste a password or access token into chat.

## 1. Create a repository

1. Click the + at the top right of github.com, then New repository.
2. Name: short, lowercase, hyphens (for example `my-plugin`).
3. Choose Public (anyone can see) or Private.
4. Tick Add a README. Choose a licence from the dropdown (see section 5).
5. Click Create repository.

An empty repo shows a "Quick setup" page with command-line boxes. A beginner can ignore everything on it and use the link "uploading an existing file" instead.

## 2. Put files in the repo (web, no Git)

On the repo page: Add file, then Upload files. Then drag files or click "choose your files".

Limits (V: GitHub docs, Adding a file to a repository):
- 25 MiB per file when uploading in the browser.
- Up to 100 files per upload.
- Larger files, up to 100 MiB each, need the command line; files above 100 MiB need Git Large File Storage.
- A protected branch cannot be edited through the web upload.
- Push protection can block a file containing a supported secret, such as a token.

Folders: the docs say you can drag a file or folder. If the user's browser will not take a folder, use one of these instead:
- Create the folder in the web editor: Add file, Create new file, type `foldername/filename.md` in the name box (typing the slash makes the folder), add content, then commit. Check the behaviour in the current UI.
- Unzip the folder and upload the files in batches that keep their folder paths, or use GitHub Desktop.
- Let the assistant push the files if it has repo access.

Zip files are stored as a single file; GitHub does not unzip them. Upload the unzipped contents.

Finish with a commit message (short, what changed) and the Commit changes button.

Check the result: open the repo page and compare the file list to what was intended. Common mistake: files land in the root instead of in their folder.

## 3. Releases with downloads (what users should download)

A release is a labelled download page based on a Git tag (V: GitHub docs, About releases).

1. On the repo page click Releases (right side), then Draft a new release.
2. Choose a tag such as `v1.0.0` (type a new one, then Create new tag).
3. Title and notes: what it is, how to install in three steps, what changed.
4. Drag the files into the assets box. Beginner-friendly releases include a built installer or file per operating system, a short manual, and install instructions, not just a bare file or the source code.
5. Click Publish release.

Limits (V): each file under 2 GiB, up to 1000 assets per release, no limit on total size or bandwidth.

Release notes template:
- What it is (one line)
- Download: pick your system (Windows, macOS, Linux)
- Install in three steps
- Checksums (SHA-256) for each file
- Known issues

## 4. Licence and README basics

- A repo without a licence is not open source; others have no right to reuse it. Pick one deliberately.
- MIT: very permissive, short. AGPL-3.0 or GPL: share-alike. Projects built on JUCE under its open-source option are covered by AGPLv3 (V: JUCE forum, staff), so check the current JUCE licence before choosing.
- Never publish vendor files (manuals, factory presets, logos, binaries) you do not own the rights to. Link to them instead.
- README must answer: what is it, how to install, how to use, licence, how to report problems.

## 5. Keep private information out (most important)

Before the first public push, search every file and the commit identity for: real name, personal email, phone, address, employer, tokens, passwords, local paths with the username.

Commit identity:
- Use the GitHub noreply address, shown in Settings, Emails, with "Keep my email addresses private" ticked. Format: `<numeric id>+<username>@users.noreply.github.com`.
- Set it before committing: `git config user.name "<username>"` and `git config user.email "<id>+<username>@users.noreply.github.com"`. Check with `git log --format='%an <%ae>'` before pushing.
- When an assistant commits for the user, it must use this identity and never the user's real email.

If private data already went public (V: GitHub docs, Removing sensitive data from a repository):
1. If it is a credential, revoke or rotate it first. That may be enough on its own.
2. Rewrite history locally with `git-filter-repo` (version 2.47 or later for `--sensitive-data-removal`). Remove a file with `--invert-paths --path`, or replace text with `--replace-text`.
3. Force-push to overwrite the repo on GitHub.
4. Contact GitHub Support to remove cached views and pull request references; give them the repo name, number of affected PRs and the first changed commits from the tool's output.
5. Forks keep the data; ask fork owners to remove it. Collaborators must rebase, not merge.
6. Warning from the docs: other people's clones keep the data, and a rewrite can reveal what was removed. Assume the data was seen.

Amending a recent commit is enough only for the branch tip; the old commit may still be reachable by its direct link until GitHub cleans up, so step 4 still applies.

## 5b. Choosing what goes public

- Research notes, captured device data, personal notes and chat transcripts do not belong in a public repo unless the user says so.
- Ask before publishing anything that was not written for the public.

## 6. Everyday tasks (one at a time)

- Edit a file on the web: open it, pencil icon, change, Commit changes.
- Delete a file: open it, three dots, Delete file, commit.
- Rename or move: edit the filename box, typing the new path; commit.
- Pin a repo to the profile: profile page, Customize your pins.
- Enable a project web page (GitHub Pages): Settings, Pages, choose the branch and folder. Check the current UI.
- Report or track problems: Issues tab. Offer an issue template for bug reports.

## 7. When something fails

- Upload refused: check file size (25 MiB web limit), number of files (100), and protected branch.
- Missing folder: files were uploaded flat; recreate the path with Create new file or re-upload.
- Rejected push with a secret warning: remove the secret, rotate it, and try again.
- Never suggest disabling security prompts.

## Sources

- GitHub docs, Adding a file to a repository: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- GitHub docs, About releases: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- GitHub docs, Removing sensitive data from a repository: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
