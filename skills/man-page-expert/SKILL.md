---
name: man-page-expert
description: Use when helping a non-programmer find, read, search or write Unix/Linux man pages (and info, tldr, --help), incl. writing and installing a man page for your own plugins or CLI tools.
---

# Man pages: reading them and writing one

Labels: VERIFIED (source) means read on a fetched page or tested here. COMMUNITY means common practice, not read on an official page. UNVERIFIED means not read; check before acting.
Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue.

## Rules of engagement
1. Explain what a command does first. Man commands only read, so they are safe.
2. One command at a time, and say what the reader should see.
3. Writing a page: the reader edits a plain text file and a tool builds the man page. No raw roff unless asked.
4. Never claim a page exists on the reader's machine. Have the reader check with `man -w name`.

## What a man page is
- A man page is the manual for one command, file format, function or topic. You open it in the terminal with `man name`.
- VERIFIED (man-pages(7), man(1)): pages are grouped into numbered sections. Section numbers are written in brackets, for example `ls(1)`.
- VERIFIED (groff manual): the `man` macro package is the most widely used roff package and most man pages are written in it.

## Sections 1 to 9
VERIFIED (man-pages(7) lists 1 to 8; man(1) lists 1 to 9):

| Section | Holds | Example idea |
|---|---|---|
| 1 | User commands you run in a shell | `ls(1)`, `man(1)` |
| 2 | System calls (kernel functions) | `open(2)` |
| 3 | Library functions (mostly libc) | `printf(3)` |
| 4 | Special files, devices in /dev | `null(4)` |
| 5 | File formats and config files | `crontab(5)` |
| 6 | Games and small programs | |
| 7 | Overviews, conventions, protocols | `man-pages(7)`, `man(7)` |
| 8 | System administration commands, often root only | `mount(8)` |
| 9 | Kernel routines, marked "Non standard" in man(1) | rare |

- VERIFIED (man-pages(7)): section 9 is not in its list. man(1) calls it non standard.
- VERIFIED (systemd.service page): systemd uses 1 for commands (systemctl(1)), 5 for unit files (systemd.unit(5)), 7 for overviews, 8 for admin tools.
- For the reader: a plugin or CLI tool you run is section 1. A config file format is section 5. A topic overview is section 7.
- The same name can exist in several sections, for example `printf(1)` and `printf(3)`. Use `man -f printf` to list them, then `man 3 printf`.

## Step 1: open a page
```
man ls
```

- VERIFIED (man(1)): if a name exists in several sections, man shows only the first one found, unless you use `-a`.
- VERIFIED (man(1)): default search order is `1 n l 8 3 0 2 3type 5 4 9 6 7`. `$MANSECT` or the SECTION line in man_db.conf can change it.
- Ask for a section: `man 5 crontab`. VERIFIED: `-s list` also works. Show all matches: `man -a printf`.
- Quit the page with `q`.

## Step 2: move around with less
VERIFIED (less(1)); man shows pages in `less` by default (man(1): default pager is less, falls back to cat):

| Key | Does |
|---|---|
| Space | page forward |
| b | page back |
| d / u | half page down / up |
| g / G | top / bottom |
| /word | search forward, Enter to start |
| ?word | search backward |
| n / N | next match / previous match, same / reverse direction |
| &word | show only lines with the word; empty `&` turns it off |
| h | less help |
| q | quit |

- VERIFIED (less(1)): search is case-sensitive by default. Option `-i` ignores case unless your pattern has capitals. Type `-i` then Enter inside less to toggle.
- Pager choice: VERIFIED (man(1)) `-P pager` beats `$MANPAGER`, which beats `$PAGER`. Example: `man -P cat ls | head -30` prints plain text with no pager.

## Step 3: find the right page
- VERIFIED (apropos(1), whatis(1), man(1)): `man -k word` is about the same as `apropos word`. It searches the one-line descriptions for the word. `man -f name` is about the same as `whatis name`. It shows the one-line description for pages with that exact name.
- VERIFIED (apropos(1)): `-a` shows only results that match all keywords. `-e` exact match. `-w` wildcard. `-r` regex, which is the default.
- VERIFIED (apropos(1), whatis(1)): both use an index database that `mandb` updates. After installing new pages, results can be missing until the index is rebuilt.
- VERIFIED (apropos(1)): exit status 16 means nothing matched.
- VERIFIED (man(1)): `-K` searches the text of all pages. It is slow, limiting to a section helps, and it searches source so it can miss or false match.
- VERIFIED (whereis(1)): `whereis name` finds the binary, source and man page files for a name. `-m` limits it to man pages (info docs are included), `-b` to binaries.
- VERIFIED (man(1)): `man -w name` prints where the page file lives, without showing it. `-a` lists all matches.

## Step 5: read the SYNOPSIS
VERIFIED (groff_man_style(7), man-pages(7)):

- Bold text: type it exactly as shown (command and option names).
- Italic or underlined text: a placeholder you replace (a file name, a number). Many terminals show italic as underline.
- Square brackets `[ ]`: optional.
- Ellipsis `...`: the thing before it may repeat.
- The groff_man_style page does not document the vertical bar; UNVERIFIED but COMMUNITY: `a | b` means choose one.

Example, read aloud: `exampletool [-v] [-o file] input...` means: run exampletool, optionally `-v`, optionally `-o` plus a file name, then one or more input names.

## Step 6: read a page fast
VERIFIED (man-pages(7) section order; Sections 1 and 8 get OPTIONS and EXIT STATUS): pages follow a standard order of headings.

1. NAME and SYNOPSIS: what it is, how to call it.
2. DESCRIPTION: what it does. Often long, skim the first paragraph.
3. OPTIONS: each flag. Search with `/-x` for one flag.
4. EXAMPLES: go here early if it exists. Copy then change.
5. EXIT STATUS: the numbers the command returns. Useful in scripts.
6. ENVIRONMENT: variables that change behavior (for example MANPATH for man).
7. FILES: config and data files it reads or writes.
8. NOTES, CAVEATS, BUGS: gotchas and known problems.
9. SEE ALSO: related pages. Best place to find the next thing to read.

VERIFIED (man-pages(7)): also possible are STANDARDS, HISTORY, VERSIONS. AUTHORS is discouraged there. Not every page has every heading.

## Other help sources
- `command --help` or `-h`: quick built-in summary. COMMUNITY: not a standard, some tools print it, some do not. UNVERIFIED for any given tool.
- `help cd` in bash: VERIFIED (Bash manual) `help [-dms] [pattern]` shows help for bash builtins. `-d` short description, `-m` man-like format, `-s` short synopsis. Builtins like `cd` often have no man page of their own because they are part of bash, see `man bash`.
- `type name`: VERIFIED (Bash manual) tells how bash would interpret a name (builtin, file, alias).
- info pages: UNVERIFIED (the info(1) page and key table were not readable). COMMUNITY: GNU tools often have a longer manual read with `info name`. Inside info: `n` next node, `p` previous, `u` up, `q` quit, `?` help. Verify with `?` on first use.
- tldr: VERIFIED (tldr-pages GitHub) community-written short pages with practical examples, a complement to man pages. Clients: `pipx install tldr`, or `brew install tlrc`, or the web client at tldr.inbrowser.app. Licence CC BY 4.0. Use it for a quick example, then man for the truth.
- systemd: VERIFIED (freedesktop.org) pages are online under /software/systemd/man/latest/. Look for `systemd.service(5)`, `systemd.unit(5)`, `systemctl(1)`, `journalctl(1)` on your machine with `man`.

## Where man pages come from (Fedora and Bazzite)
- Package that provides `man`: man-db (COMMUNITY on Fedora; UNVERIFIED for this exact package split; check with `rpm -q man-db`).
- Linux kernel and libc pages (sections 2 and 3, plus 4, 5, 7): man-pages package. VERIFIED that the man-pages project exists (man7.org man-pages(7)). UNVERIFIED which Fedora package carries which page.
- Each program installs its own page, normally under `/usr/share/man/manN/`. VERIFIED (hier.7): man pages go in /usr/share/man in subdirectories by section.
- Flatpak apps: UNVERIFIED. COMMUNITY: they usually have no man page on the host. Look for a Help menu or the app website. Do not promise a man page.
- Bazzite and other immutable systems: UNVERIFIED for man pages specifically. COMMUNITY: /usr is read-only, so you cannot just drop pages into /usr/share/man. For tools in a Distrobox container, run `man` inside the container: `distrobox enter <name>`, then `man tool`. Bazzite docs on Distrobox are covered by the bazzite-kde-linux skill. Check that `man -w ls` works first.

## Online mirrors
- VERIFIED fetched: man7.org (Linux man-pages and groff pages), mandoc.bsd.lv (mdoc, mandoc), man.archlinux.org, freedesktop.org (newest systemd, read page said systemd 262).
- UNVERIFIED (blocked): manpages.debian.org, linux.die.net. COMMUNITY quality note: linux.die.net is a static mirror and often old. Check the date and version before trusting an option list.
- A web page may not match the version on the reader's machine. Local `man tool` is the truth.

## Troubleshooting: "No manual entry for X"
Go in order. Stop when it works.

1. Check the spelling and try a section: `man 1 name`, then `man -k name`.
2. Is the program there? `which name` or `whereis name`. VERIFIED (whereis(1)) searches binaries, sources and man pages in standard places plus $PATH and $MANPATH.
3. Does a page exist? `man -w name`. VERIFIED (man(1)): prints the page file path, or nothing found.
4. Is it a shell builtin? Try `help name`.
5. Is the package missing its docs? COMMUNITY: some packages put man pages in a separate "doc" package. UNVERIFIED for Fedora. Ask me to check the package.
6. Is the index stale, so `apropos` is empty but `man name` works? Rebuild it: `sudo mandb`. VERIFIED (mandb(8)): `mandb` creates or updates the index caches. `-c` deletes and rebuilds from scratch (use if corrupt), `-q` quiet, `-u` user databases only. Global cache: `/var/cache/man/`.
7. Is `$MANPATH` wrong? `echo $MANPATH`. VERIFIED (man(1)): if MANPATH is set, its value is the search path. If empty, man uses its config. Fix by unsetting: `unset MANPATH`. A custom path: `man -M /some/dir name` (UNVERIFIED `-M` here; whatis(1) shows `-M path` overrides $MANPATH).
8. Immutable system, tool inside a container or Flatpak: see the Bazzite note above.
9. Still stuck: look at the `man -w` and `echo $MANPATH` output and decide.

Exit codes of man (VERIFIED man(1)): 0 ok, 1 usage or config error, 2 operational error, 3 child process failed, 16 page or keyword not found.

## Writing a man page: pick a route
Three options, easiest first:

| Route | Source file | Tool | Notes |
|---|---|---|---|
| Markdown | `name.1.md` | pandoc | VERIFIED. Closest to plain writing. pandoc 3.1.3 tested here. |
| scdoc | `name.1.scd` | scdoc | VERIFIED syntax (scdoc(5)). Small, simple, made for man pages. |
| ronn | `name.1.ronn` | ronn-ng | VERIFIED exists (GitHub). Needs Ruby 2.4 or newer. |
| roff (man macros) | `name.1` | none | VERIFIED. Hand written. Most control. |

COMMUNITY: for the reader, pandoc or scdoc. Pandoc is also good for README text. Install on Bazzite per the install order in the bazzite-kde-linux skill (Homebrew for CLI tools; UNVERIFIED that pandoc or scdoc are in brew, check with `brew search`).

### Route A: Markdown with pandoc (VERIFIED by test, pandoc 3.1.3)
Make `exampletool.1.md`:

```
% EXAMPLETOOL(1) exampletool 1.0 | Example Tools Manual
% Example Author
% October 2026

# NAME

exampletool - process files

# SYNOPSIS

**exampletool** [**-v**] [**-o** *file*] *input*...

# OPTIONS

**-v**
:   Verbose.

**-o** *file*
:   Write output to *file*.
```

Build: `pandoc -s -f markdown -t man exampletool.1.md -o exampletool.1`

- VERIFIED (pandoc demo example 10): `pandoc -s -t man pandoc.1.md -o example10.1`. `-s` means standalone, which writes the header.
- VERIFIED (tested; pandoc's manual text on this was not readable): line 1 `% NAME(section) middle | header` gave `.TH "EXAMPLETOOL" "1" "October 2026" "exampletool 1.0" "Example Tools Manual"`. Line 2 (author) became an AUTHORS section. Line 3 (date) went into the footer. Each `# HEADING` became `.SH`. The `:` definition list became `.TP` option entries. Bold became `\f[B]`, italic `\f[I]`.

### Route B: scdoc (VERIFIED, scdoc(5))
First line: `NAME(section) ["left_footer" ["center_header"]]`. Headings `# NAME`, `## Sub`. Bold `*text*`. Underline `_text_`. Lists start with `- ` and numbered with `. `. Literal blocks use triple backticks. Comment lines start with `; `. A backslash makes the next character literal.

```
exampletool(1) "Example Author" "Example Tools Manual"

# NAME

exampletool - process files

# SYNOPSIS

*exampletool* [*-v*] [*-o* _file_] _input_...
```

Build: `scdoc < exampletool.1.scd > exampletool.1` (VERIFIED, scdoc(1): reads stdin, writes roff to stdout).

### Route C: roff by hand with the man macros
VERIFIED (groff_man(7), groff_man_style(7)):

- `.TH identifier section [footer-middle [footer-inside [header-middle]]]`. Call it once, before any other macro. Section may be left out only in the old rule for 1 to 9 as header-middle; give it anyway.
- `.SH` section heading, `.SS` subsection.
- `.PP` new paragraph. `.TP` tagged paragraph: the next line is the tag, the lines after are the indented text. Used for option lists. `.TQ` adds a second tag.
- `.B` bold, `.I` italic. `.BR` `.IR` `.BI` and other pairs alternate fonts with no space between. Quote arguments that have spaces.
- `.EX` and `.EE` wrap examples (no filling, monospaced). `.RS` `.RE` indent a block.
- `.SY` and `.YS` build a synopsis. `.MR` writes a cross reference like `name(5)`.
- Deprecated, avoid in new pages: AT, DT, OP, PD, SB, UC.
- The first section must be NAME, right after TH, with only the name and a short summary (for indexers like mandb).
- Escape each option dash as `\-`. Start a text line that would begin with a dot or apostrophe with `\&`. No blank lines in the source; use a lone `.` instead. Comments: `.\" text`.

### mdoc or man macros?
- VERIFIED (mdoc(7), mandoc(1)): mdoc is a semantic macro language that starts with `.Dd`, `.Dt`, `.Os`, then `.Sh NAME`, `.Nm`, `.Nd`. mandoc detects the language per file by the first macro.
- VERIFIED (groff manual): most pages use the man macros. For the reader: man macros or Markdown. Skip mdoc.

## Preview, lint, install
1. Preview without installing. VERIFIED (man(1)): `-l` formats and shows a local source file. `man -l exampletool.1`. VERIFIED (groff manual): the long form is `groff -t -man -Tutf8 exampletool.1 | less`.
2. Lint. VERIFIED (mandoc(1)): `mandoc -T lint exampletool.1` only parses and prints messages. It implies `-W all`. `-W style` adds style hints. Exit 1 means base or style notes, higher means warning or error. Install mandoc via Homebrew or Distrobox (UNVERIFIED which). Not found? Preview and read the output by eye.
4. Install for yourself only (no root):
   - UNVERIFIED path details. VERIFIED (hier(7)): `/usr/local/man` holds pages for locally installed programs; `/usr/share/man` is the system tree, `/usr/man` is obsolete. The hier(7) page had no entry for `/usr/local/share/man`.
   - COMMUNITY: put the file in `/usr/local/share/man/man1/exampletool.1` (the folder for section 1). Create the folder if needed.
   - UNVERIFIED on Bazzite: whether /usr/local is writable (often a link into /var). Check with `ls -ld /usr/local` before sudo.
   - Safer personal option, COMMUNITY: keep pages in `~/.local/share/man/man1/` and run `man -M ~/.local/share/man exampletool` or add it to `MANPATH`. VERIFIED (mandb(8)): `-u` builds user databases. UNVERIFIED that man finds ~/.local/share/man on its own.
6. Update the index: `sudo mandb` (VERIFIED, mandb(8)), then `man -w exampletool` should print the path and `apropos exampletool` should find it.

## Style conventions
VERIFIED (man-pages(7)):

- Command names and options: bold. Arguments and file names: italic. A reference to a page: name in bold followed by the section in roman, for example **ls**(1).
- Standard heading order: NAME, SYNOPSIS, DESCRIPTION, OPTIONS, EXIT STATUS, ENVIRONMENT, FILES, STANDARDS, HISTORY, NOTES, CAVEATS, BUGS, EXAMPLES, SEE ALSO.
- Gender-neutral language, American spelling, "man page" not "manpage", "terminal" not "tty", no e.g./i.e./etc. in running text.
- Semantic newlines: one sentence per line, split long ones at phrase breaks. This makes diffs readable.
- Source lines near 75 characters. In shell examples only the user's typing is bold.

COMMUNITY advice for the reader:

- NAME line: `name \- one line, no full stop`. Short, lowercase start.
- Put two or three real EXAMPLES. Test each one yourself.
- For a plugin: say where the plugin file is installed, what its parameters are, and which hosts it was tested in. Mention FILES (presets, config).

## Packaging notes
- VERIFIED (hier.7): man pages live under /usr/share/man/manN/ for distribution packages.
- RPM (Fedora): UNVERIFIED. The Fedora packaging guideline pages were blocked (Anubis). COMMUNITY: the spec file installs pages under the man directory macro (`%{_mandir}/man1/`) and lists them in `%files`. VERIFIED only that `rpm-macros(7)` is the place to look up the macro values; its page content was not readable.
- DEB (Debian): UNVERIFIED. The Debian policy page was blocked. COMMUNITY: pages go in `/usr/share/man/man1/` and are gzip compressed; Debian wants one for each command.
- Ship both: the source (`.1.md` or `.1.scd`) in the repo, and the built `.1` file in release builds, so users do not need pandoc.
- COMMUNITY: a plugin has no command line, so use a README and in-app help. Man pages fit CLI tools.

## Copyable template (Markdown for pandoc)
```
% MYTOOL(1) mytool 0.1 | Example Manual
% Your Name
% October 2026

# NAME

mytool - one short line about what it does

# SYNOPSIS

**mytool** [**-h**] [**-v**] [**-o** *file*] *input*...

# DESCRIPTION

**mytool** reads each *input* and does the thing.
Say what it does in one or two plain sentences.

# OPTIONS

**-h**
:   Show help and exit.

**-v**
:   Print more detail.

**-o** *file*
:   Write the result to *file*.

# EXAMPLES

Run it on one file:

    mytool song.wav

# EXIT STATUS

0 on success, 1 on any error.

# SEE ALSO

**sox**(1)
```

- Replace names, then build with `pandoc -s -f markdown -t man mytool.1.md -o mytool.1`. Preview with `man -l mytool.1`.
- The title block was tested (VERIFIED, pandoc 3.1.3). The indented code example is UNVERIFIED in pandoc output; check the preview.

## Not verified
- Fedora/Bazzite specifics: package names (man-db, man-pages), man-pages in a separate doc package, Flatpak having no man pages, Distrobox man workflow, Homebrew man path, /usr/local writability on Bazzite. Fedora docs were blocked (Anubis).
- Fedora and Debian packaging rules for man pages (paths, compression, required pages). Debian policy page was blocked.
- manpages.debian.org and linux.die.net content and age (blocked); the quality note is COMMUNITY.
- info reader key table and info(1) text (page not readable). tldr details beyond the GitHub README.
- pandoc manual text on the man title block (only the tested output was used). ronn-format(7) first line syntax.
- Whether man finds `~/.local/share/man` without MANPATH; man-db docs site and Reddit r/linux4noobs were not fetched.
- The meaning of `a | b` in synopses (groff_man_style does not document it).

## Sources (fetched)
- https://man7.org/linux/man-pages/man7/man-pages.7.html
- https://man7.org/linux/man-pages/man1/man.1.html (man-db man(1))
- https://man7.org/linux/man-pages/man7/man.7.html and groff_man.7.html
- https://man7.org/linux/man-pages/man7/groff_man_style.7.html
- https://man7.org/linux/man-pages/man8/mandb.8.html
- https://man7.org/linux/man-pages/man1/apropos.1.html, whatis.1.html, whereis.1.html, less.1.html
- https://man7.org/linux/man-pages/man7/hier.7.html
- https://mandoc.bsd.lv/man/mdoc.7.html and mandoc.1.html
- https://www.gnu.org/software/groff/manual/groff.html
- https://pandoc.org/MANUAL.html and https://pandoc.org/demos.html (plus a local pandoc 3.1.3 test)
- https://man.archlinux.org/man/scdoc.5 and scdoc.1
- https://github.com/apjanke/ronn-ng and https://github.com/tldr-pages/tldr
- https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html
- https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html
