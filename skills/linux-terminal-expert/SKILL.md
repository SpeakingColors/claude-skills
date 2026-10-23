---
name: linux-terminal-expert
description: Use when helping a non-programmer work safely in the Linux terminal and bash, covering navigation, text tools, pipes, scripts, ssh, tmux, cron, archives, processes and Bazzite package commands.
---

# Linux terminal and shell for a non-programmer

Labels: VERIFIED (source) = read on a fetched page. COMMUNITY = common practice, not read on a page. UNVERIFIED = from memory, check before relying on it.
Scope: the shell and command-line workflow only. Man-page reading and general Linux/Bazzite admin live in other skills.

## Rules of engagement

1. Assume the reader is not a programmer. Plain words first, then one exact step. One change at a time, ask the reader to test, then continue. Explain in plain words first, then give one command, then say what it will do.
2. One step at a time. Wait for the output before the next step.
3. Prefer read-only commands first (ls, cat, less, grep, du, df, ps). Change things second.
4. Preview before any delete or bulk change (see Safe habits).
5. Never ask the reader to paste a command they do not understand. Never pipe a download into a shell.
6. If an answer is UNVERIFIED, say so and point to explainshell.com or `man <cmd>`.

## Terminal vs shell vs prompt

- VERIFIED (Greg's Wiki BashGuide): the shell is a command interpreter, "a layer between system function calls and the user". Bash "is not your terminal".
- The terminal is the window (here Konsole). The shell (bash) runs inside it and reads what you type.
- bash is the common default. zsh and fish are other shells. UNVERIFIED: which shell Bazzite KDE gives the reader. Check with `echo $SHELL`.
- COMMUNITY: fish has friendlier autosuggest but different syntax. Scripts written for bash will not all run in fish. Keep scripts as bash with a shebang.
- Reading a prompt: UNVERIFIED (PS1 page not fetched). Typical shape is `user@host:folder$`. `~` means home. `$` is a normal user. `#` means root.
- Check the folder with `pwd`. Check who you are with `whoami`.

## Navigation and files

Step 1: look around. VERIFIED (tldr ls, cd):
```
pwd                 # where am I
ls -la              # long list, hidden files too
ls -lh              # human sizes
ls -ltr             # oldest first, newest last
cd ~                # home;  cd -  = previous folder;  cd ..  = up
mkdir -p a/b/c      # make nested folders
```
Copy and move. VERIFIED (GNU coreutils cp, mv): both overwrite existing files by default.
- cp: `-r` copies folders, `-a` keeps attributes, `-i` asks before overwrite, `-n` never overwrites, `-v` shows each file.
- mv: `-i` asks, `-n` never overwrites, `-v` shows each file.
- Habit: `cp -iv src dest` and `mv -iv src dest`.
- Tab completes names. Quote or backslash names with spaces.

Delete safely. VERIFIED only that rm is the delete command; the GNU rm page failed to load, so flag details are UNVERIFIED.
- rm does not use a trash. COMMUNITY: no undo. UNVERIFIED: GNU rm `-I` prompts once before bulk deletes; check `man rm`.
- Preview first: `ls <same pattern>`, then `rm -v <pattern>`.
- Prefer KDE Trash from Dolphin, or the `trash-cli` tool, for things you might want back (UNVERIFIED availability).
- Never run `rm -rf` with a variable you did not print first.

Find things.
- VERIFIED (tldr find): `find DIR -name '*.ext'`, `-iname` for any case, `-type d` for folders, `-maxdepth 1`, `-size +500k`, `-not -path '*/x/*'`.
- VERIFIED: `find ... -empty -delete -print` deletes. Run it WITHOUT `-delete` first.
- VERIFIED (tldr locate): locate uses a database that refreshes daily or weekly; `sudo updatedb` rebuilds it. Quote the pattern.
- VERIFIED (tldr fd): `fd "regex"` is a friendlier find if installed.
- VERIFIED (Greg's Wiki ParsingLs): do not parse `ls` output in scripts. Use globs or `find -print0`.

## Text tools

All VERIFIED from tldr pages unless noted.
```
less file               # q quits, /word searches, n next, G end, g start, F follow
head -n 20 file         tail -n 20 file         tail -f file   # follow a log, Ctrl+C stops
grep -rI "word" DIR     # search recursively, skip binaries
grep -n -i "word" file  # line numbers (-n), ignore case (-i)
grep -F "a.b" file      # literal text, not a pattern
grep -v "word"          # lines NOT matching;  grep -C 3 = 3 lines of context
rg "word"               # ripgrep: recursive by default; -l lists files; -g '*.md' filters
sort file | uniq -c | sort -nr     # count repeats, most common first
cut -d ',' -f 1,3 file             # columns from a CSV-like file
tr 'a-z' 'A-Z' < file              # swap characters;  tr -d '\r' removes Windows line ends
wc -l file                         # count lines
diff -u old new                    # show changes;  diff -rq dirA dirB  = which files differ
sed 's/old/new/g' file             # replace in output; the file is NOT changed
awk '{print $2}' file              # print the second column
```
- uniq only joins neighbours, so sort first (VERIFIED, tldr uniq).
- sed `-i` edits the file in place. UNVERIFIED on this machine: always test without `-i` first, or `cp file file.bak`.

## Pipes, redirection, quoting, globs, variables, PATH

- Pipe `|` sends one command's output into the next. VERIFIED (tldr usage above); the GNU Pipelines page failed to load.
- VERIFIED (GNU Bash manual, Redirections): `>` writes a file and truncates it to zero size, `>>` appends, `<` reads, `2>` sends errors, `&>` sends both, `2>&1` makes errors follow output.
- VERIFIED: order matters. `cmd > f 2>&1` sends both to f. `cmd 2>&1 > f` does not.
- Danger: `>` on an existing file destroys it. Use `>>` or a new name.
- VERIFIED (Greg's Wiki Quotes): double-quote every expansion. `cp -- "$src" "$dest"`, not `cp $src $dest`. Single quotes are fully literal. A backslash escapes one character.
- VERIFIED (Greg's Wiki glob): `*` is any string, `?` is one character, `[abc]` one of a set. Dotfiles are not matched by `*`. A glob with no match stays as literal text unless `nullglob` is set. Globs do not split names with spaces.
- Variables: `name="value"` with no spaces around `=`; read it as `"$name"`. UNVERIFIED in detail (Shell-Variables page failed).
- Environment variable for one command: `LANG=C sort file`. Export for children: `export NAME=value`. COMMUNITY.
- PATH is the list of folders searched for commands. See it with `echo "$PATH"`. UNVERIFIED (GNU page failed). To run a script in the current folder use `./script.sh`.
- Add a folder to PATH in `~/.bashrc`: `export PATH="$HOME/bin:$PATH"` (COMMUNITY), then open a new terminal.

## History and shortcuts

- VERIFIED (GNU Bash manual): readline keys: Ctrl+A start of line, Ctrl+E end, Alt+B / Alt+F back or forward a word, Ctrl+L clear screen, Ctrl+K kill to end, Ctrl+U kill to start, Ctrl+W kill word behind, Ctrl+Y paste what you killed.
- UNVERIFIED (page failed): Ctrl+R searches history backward; type part of a command, press Ctrl+R again for older matches.
- VERIFIED (GNU Event Designators): `!!` repeats the last command, `!string` the last one starting with string, `^old^new^` repeats it with a swap.
- VERIFIED (tldr sudo, history): `sudo !!` repeats the last command with sudo. A leading space keeps a command out of history (shell setting dependent, UNVERIFIED). `history 20` shows the last 20.
- VERIFIED: history is saved in `~/.bash_history` (HISTFILE), size set by HISTSIZE (default 500).
- Ctrl+C stops a running command. Ctrl+D ends input or logs out. Tab completes.
- Konsole: VERIFIED (KDE UserBase): Shift+Ctrl+T new tab; double-click a tab to rename it. UNVERIFIED: Ctrl+Shift+C / Ctrl+Shift+V copy and paste; split view under View menu; Settings, Edit Current Profile for fonts. Ctrl+C in a terminal stops commands, it does not copy.

## Job control, tmux, screen

- VERIFIED (GNU Job Control): Ctrl+Z stops the foreground job; `jobs` lists; `bg` continues it in the background; `fg` brings it back; `cmd &` starts in the background; `%1 &` resumes job 1.
- VERIFIED (tldr nohup): `nohup cmd > out.log &` keeps running after the terminal closes.
- tmux: VERIFIED (man7 tmux, tldr tmux). Prefix is Ctrl+B. Press the prefix, release, then a key.
```
tmux new -s work       # start a named session
Ctrl+B then d          # detach, it keeps running
tmux ls                # list sessions
tmux attach -t work    # come back
Ctrl+B then c          # new window;  " splits top/bottom;  % splits left/right
tmux kill-session -t work
```
- screen: VERIFIED (tldr screen): `screen -S name`, detach `Ctrl+A d`, `screen -ls`, `screen -r name`.
- Use tmux for long jobs over ssh so a dropped connection does not kill them. COMMUNITY.

## ssh basics

- VERIFIED (man7 ssh): `ssh [user@]host [command]`; `-p PORT`; `-i keyfile`; `-v` for debug (up to `-vvv`); `-L local:host:remote` forwards a port.
- VERIFIED: first connect shows the server key fingerprint; accepted keys go to `~/.ssh/known_hosts`; a changed key triggers a warning. Do not ignore that warning without asking the owner.
- VERIFIED: per-user config is `~/.ssh/config` and needs strict permissions. Keys are made with `ssh-keygen`; the public key goes in `~/.ssh/authorized_keys` on the server.
- Copy files: `rsync -a --dry-run src/ user@host:dest/` first (VERIFIED, tldr rsync mentions `--dry-run`, `-a`, `user@host:path`). Then run without `--dry-run`.
- Trailing slash on rsync source matters. UNVERIFIED here; test with `--dry-run`.

## sudo and permission errors

- VERIFIED (tldr sudo): sudo runs one command as superuser; `sudo -e file` edits a root file safely; `sudo -i` opens a root shell (avoid).
- "Permission denied": read it, do not just add sudo. Check `ls -l file` and `whoami`.
- VERIFIED (man7 chmod): `chmod` symbolic form `[ugoa][+-=][rwx]`; numeric is octal (4 read, 2 write, 1 execute for owner, group, others). `-R` is recursive.
- VERIFIED (tldr chmod): `chmod u+x script.sh` makes your own script runnable. `chmod -R` on a wrong folder can break a system, so name the folder fully.
- VERIFIED (tldr chown): `sudo chown user:group path`. Never run `chmod -R` or `chown -R` on `/`, `/usr`, `/etc` or all of `$HOME`.
- On Bazzite, `/usr` is read-only by design. "Read-only file system" there is normal, not a bug. COMMUNITY (see bazzite-kde-linux skill).

## Scripts

Step 1: make a file, e.g. `~/bin/backup.sh`. UNVERIFIED layout, COMMUNITY style:
```
#!/usr/bin/env bash
set -euo pipefail
src="$HOME/Music/projects"
dest="$HOME/backup"
mkdir -p "$dest"
for f in "$src"/*.als; do
  cp -iv -- "$f" "$dest/"
done
```
Step 2: `chmod u+x ~/bin/backup.sh`, then `shellcheck ~/bin/backup.sh`, then run it.
- Shebang `#!/usr/bin/env bash` on line 1 picks the interpreter. COMMUNITY.
- VERIFIED (GNU Set Builtin): `-e` exits on a failing command, `-u` treats unset variables as errors, `-o pipefail` makes a pipeline fail if any part fails (return value of the last non-zero command).
- UNVERIFIED: `set -e` has surprising exceptions (inside `if`, `&&` chains). It is a safety net, not a guarantee.
- VERIFIED (GNU Looping, Functions): `for x in a b c; do echo "$x"; done`. Function: `name () { commands; }`, and inside it `$1` is the first argument.
- VERIFIED (ShellCheck wiki): ShellCheck is a static analysis tool; run `shellcheck script`. SC2086 flags unquoted expansions: use `"$1"` and `"$@"`, or an array for option lists.
- Install: VERIFIED (ShellCheck README): `dnf install ShellCheck`, `brew install shellcheck`. On Bazzite prefer `brew install shellcheck` (COMMUNITY, see packages).
- Test scripts on a copy of the data first.

## Scheduling: cron vs systemd timers

- VERIFIED (man7 crontab): five fields: minute 0-59, hour 0-23, day of month 1-31, month 1-12, day of week 0-7 (0 and 7 Sunday). Ranges `8-11`, lists `1,2,5`, steps `0-23/2`. `@reboot`, `@daily` (= `0 0 * * *`).
- VERIFIED: cron sets SHELL to /bin/sh. Output is mailed to the owner unless MAILTO is empty. Edit with `crontab -e` (UNVERIFIED: edit command not on the fetched page).
- UNVERIFIED: cron's PATH is minimal. Use full paths to commands in cron lines.
- VERIFIED (man7 systemd.timer): `foo.timer` activates `foo.service` by default. `OnCalendar=` is wall-clock time. `OnBootSec=` is time after boot. `Persistent=true` catches up missed runs (OnCalendar only).
- COMMUNITY: on Bazzite prefer a user systemd timer (`systemctl --user`) so missed runs are caught up and logs go to `journalctl --user`. UNVERIFIED on this machine; check cronie is installed before relying on cron.

## Archives and compression

- VERIFIED (tldr tar): `tar czf out.tar.gz DIR` makes; `tar xf in.tar.gz -C DEST` extracts; `tar tvf in.tar` lists WITHOUT extracting; `tar caf out.tar.xz files` picks compression from the name.
- VERIFIED (tldr zip, unzip): `zip -r out.zip DIR`; `unzip -l f.zip` lists; `unzip f.zip -d DEST`.
- VERIFIED (tldr gzip, xz): both replace the original unless `-k` is given.
- Habit: list (`tar tvf`, `unzip -l`) before extracting an archive from the internet. COMMUNITY.

## Disk usage

- VERIFIED (tldr du): `du -sh DIR` total of one folder; `du -h -d 1 DIR` one level down.
- VERIFIED (tldr df): `df` shows filesystem space. UNVERIFIED: `df -h` for human sizes.
- VERIFIED (tldr ncdu): `ncdu` or `ncdu DIR` is an interactive size browser. UNVERIFIED: delete key inside ncdu; read before pressing.
- `du -h -d 1 ~ | sort -h` finds the big folders. `sort -h` is UNVERIFIED.

## Processes

- VERIFIED (tldr ps): `ps aux`; `ps aux | grep [s]tring` (the brackets stop grep matching itself).
- VERIFIED (tldr htop): `htop` live view; `htop -u name`; F1 or ? for help. `top` is the built-in older tool (UNVERIFIED details).
- VERIFIED (man7 kill, tldr kill): kill sends TERM by default, which lets the program clean up. Use KILL (-9) only if TERM fails. `kill -l` lists signals. `kill %1` stops background job 1.
- VERIFIED (tldr pgrep, pkill): `pgrep -a name` finds PIDs; `pkill name` signals by name. Run `pgrep -a name` first to see what pkill would hit.
- Never kill a process you cannot name. Never `kill -9 1` or kill the desktop session by guess.

## Network tools

- VERIFIED (tldr curl): `curl URL` prints; `curl -L -O URL` follows redirects and saves; `-v` verbose. `-k` skips certificate checks: avoid.
- VERIFIED (tldr wget): `wget URL`; `-O file`; `-c` continues an interrupted download.
- VERIFIED (man7 ss): `ss -tulnp` is the usual combination: TCP, UDP, listening, numeric, show process (each flag read separately). Process names for other users need sudo (UNVERIFIED).
- VERIFIED (tldr ping): `ping -c 4 host` stops after 4.
- VERIFIED (tldr dig): `dig +short example.com`; `dig +short example.com MX`; `dig @1.1.1.1 example.com` asks a chosen DNS server.
- Order for "no internet": ping a router IP, ping 1.1.1.1, ping a name, dig the name. COMMUNITY.
- Check a download before running it: `sha256sum file` and compare to the site's published hash. UNVERIFIED.

## Packages on Bazzite and distrobox

- VERIFIED (Bazzite docs): Flatpak (Bazaar app store) for apps; Homebrew for command-line tools; Distrobox for other Linux apps; rpm-ostree layering is discouraged "if possible".
- VERIFIED (Flatpak docs): `flatpak search NAME`, `flatpak install flathub ID`, `flatpak run ID`, `flatpak list --app`, `flatpak update`, `flatpak uninstall ID`.
- VERIFIED (rpm-ostree handbook): `rpm-ostree status` lists deployments; `upgrade` stages an update for next boot; `install PKG` layers a package and needs a reboot; `uninstall PKG` removes it; `rollback` swaps back to the previous deployment (reboot to boot it).
- VERIFIED (Bazzite docs): `rpm-ostree rollback` and the Bazzite Rollback Helper exist. `ujust update` is UNVERIFIED on the docs page.
- VERIFIED (distrobox.it): `distrobox create -n test`, `distrobox enter test`, `distrobox list`, `distrobox rm test`. Containers share your home folder.
- `dnf` does not install into the Bazzite base system. Inside a distrobox it works on the container (COMMUNITY).
- Look for the Flatpak or brew version first. Layering last.

## Safe habits

1. Read before running. Paste unknown commands into explainshell.com (VERIFIED: it matches each argument to its help text) or `man cmd` first.
2. Never `curl ... | bash` or `sudo` something from a forum without understanding it. COMMUNITY.
3. Dry run: `rsync --dry-run`, `ls PATTERN` before `rm PATTERN`, `find` without `-delete` first, `echo rm -rf "$dir"` to see what a variable expands to.
4. Backup before bulk edits: `cp -a dir dir.bak`, or `sed` without `-i`, or `tar czf` of the folder.
5. Use full paths and quotes. Check `pwd` before relative deletes.
6. One change, test, then the next. Keep the old command text in history.
7. Use `--` before names that start with `-` (VERIFIED in the Quotes page example `cp -- "$src" "$dest"`).
8. Reddit r/commandline and r/bash were blocked, so no community-rule claims here.

## Commands that can wipe your own data (a safety list, for protecting yourself)

COMMUNITY unless marked.
- `rm -rf` anything, especially with variables, `*`, `/`, `~` or `..`.
- `chmod -R` or `chown -R` on system folders; `chmod 777`.
- `> file` on an important file (VERIFIED: truncates it). `sed -i` without a backup.
- `dd if=... of=/dev/...`: writes raw to a disk. Wrong target wipes it.
- `mkfs`, `fdisk`, `parted`, `wipefs` on the wrong device. Check `lsblk` first (UNVERIFIED).
- `kill -9`, `pkill` with a loose name; `sudo` with anything you did not read.
- `curl URL | sh` or `| sudo bash`.
- Any unknown one-liner pasted from a forum or chat: read it first and ask what each part does before running.
- `find ... -delete` or `-exec rm` without a dry run (VERIFIED -delete exists).
- `rpm-ostree` changes without knowing rollback; `systemctl disable` on system units you did not name.

## Worked examples (build up one step at a time)

1. Find which log lines mention an error, newest last. Commands VERIFIED individually (tldr grep, tail, sort, uniq):
   - Step 1: `tail -n 200 file.log` (look first).
   - Step 2: `grep -i "error" file.log | tail -n 20`.
   - Step 3: `grep -i "error" file.log | sort | uniq -c | sort -nr | head` (most common errors).
2. Find big files in Downloads, then decide by hand:
   - `du -ah ~/Downloads | sort -h | tail -n 15` (`sort -h` UNVERIFIED), or `ncdu ~/Downloads` (VERIFIED).
3. Rename many files safely (COMMUNITY pattern, loop VERIFIED in GNU Looping page):
   - Step 1: `for f in *.wav; do echo mv -n -- "$f" "new_$f"; done` (echo only prints).
   - Step 2: remove `echo` only when the printed list looks right.
4. Search a project for a word and open the hit: `rg -n "word"`, then `less +NUMBER file` (UNVERIFIED `+N`).
5. Save command output and errors for a bug report: `cmd > out.txt 2>&1` (VERIFIED order), then `less out.txt`.
6. Run a long copy that survives a closed laptop lid or dropped ssh: `tmux new -s copy`, run rsync inside, `Ctrl+B d` (VERIFIED).

## Troubleshooting trees

"command not found":
1. Check spelling and case. Tab-complete it.
2. `command -v NAME` (UNVERIFIED) shows if it exists. Nothing printed means not on PATH.
3. Script in the current folder? Use `./NAME` (COMMUNITY).
4. Not installed? Order: Flatpak, brew, distrobox, then layering (VERIFIED Bazzite docs).
5. Installed by brew just now? Open a new terminal so PATH reloads (COMMUNITY).

"Permission denied":
1. `ls -l FILE` and `whoami` (read-only, VERIFIED ls).
2. Script without execute bit? `chmod u+x FILE` (VERIFIED tldr).
3. Folder you do not own? Do not chmod -R it. Ask why first.
4. Only then consider `sudo` for that single command (VERIFIED tldr sudo).

"No such file or directory":
1. `pwd` and `ls`. Wrong folder is the usual cause.
2. Spaces in the name? Quote it (VERIFIED Quotes page).
3. A glob that matched nothing stays literal, so `ls *.c` fails (VERIFIED glob page).
4. Windows line ends in a script (`^M`)? `tr -d '\r' < in > out` (VERIFIED tr flag; cause is COMMUNITY).

Command seems stuck:
1. Is it waiting for input? Ctrl+D ends input. Ctrl+C interrupts (COMMUNITY).
2. Stopped by accident (Ctrl+Z)? `jobs`, then `fg` (VERIFIED).
3. Still stuck? Another terminal: `pgrep -a NAME`, then `kill PID`, and only later `kill -9 PID` (VERIFIED man7 kill).

Disk full:
1. `df -h` to find the full filesystem.
2. `du -h -d 1 ~ | sort -h` or `ncdu ~` to find the cause.
3. Flatpak leftovers and old container data are common causes (UNVERIFIED); do not delete by guess.

ssh will not connect:
1. `ssh -v user@host` and read the last lines (VERIFIED -v).
2. `ping host`, then `dig +short host` (VERIFIED) to split network from DNS.
3. Wrong port? `-p PORT` (VERIFIED). Wrong key? `-i FILE` (VERIFIED).
4. Host key changed warning: stop and confirm with the server owner (VERIFIED warning exists).

Output scrolls away: pipe to `less`, or `cmd 2>&1 | less` for errors too (VERIFIED redirect semantics, COMMUNITY habit).

Weird characters after a binary file was printed: type `reset` and press Enter (UNVERIFIED).

## Cheat sheet: 40 commands

pwd, ls -la, cd, mkdir -p, cp -iv, mv -iv, rm -v (after ls), ln -s, find -name, locate, cat, less, head, tail -f, grep -rn, rg, sed 's///', awk '{print $1}', sort, uniq -c, cut -d -f, tr, wc -l, diff -u, tee, xargs (UNVERIFIED), history, chmod u+x, sudo, tar czf / xf, zip/unzip, du -sh, df -h, ncdu, ps aux, htop, kill, pgrep -a, curl -L -O, ss -tulnp, ping -c 4, dig +short, ssh, rsync -a --dry-run, tmux, flatpak, brew, distrobox, rpm-ostree status, shellcheck.
(All have a VERIFIED tldr or man7 line above except those marked UNVERIFIED.)

## Not verified

- GNU Bash manual pages Pipelines, Shell-Variables, Commands-For-History and the single-page manual failed to fetch. PATH, PS1 and Ctrl+R details are from memory.
- GNU coreutils rm page failed; rm flags such as -I are UNVERIFIED.
- Konsole manual (docs.kde.org) failed; only UserBase tab notes were read. Copy/paste and split-view keys UNVERIFIED.
- Fedora docs returned Access Denied. No dnf/Fedora claims verified.
- Reddit r/commandline and r/bash blocked. explainshell was read only for its description, not for sample output.
- zsh and fish behaviour not fetched. Bazzite default shell, `ujust` commands, `brew` usage, cron/cronie availability, user systemd timers, `trash-cli`, `ss` root requirement, `df -h`, `sort -h`, `sha256sum` are UNVERIFIED.
- Greg's Wiki BashFAQ on `set -e` pitfalls was not read.
- Man pages are not Bazzite-specific; versions on the reader's machine may differ.

## Sources (fetched)

- GNU Bash manual: gnu.org/software/bash/manual/html_node/ (The-Set-Builtin, Redirections, Bash-History-Facilities, Commands-For-Moving, Commands-For-Killing, Job-Control-Basics, Shell-Functions, Looping-Constructs, Event-Designators)
- GNU coreutils: cp-invocation, mv-invocation
- Greg's Wiki: mywiki.wooledge.org/BashGuide, /Quotes, /glob, /ParsingLs
- man7.org: tmux(1), crontab(5), systemd.timer(5), ssh(1), chmod(1), ss(8), kill(1)
- tldr pages (raw.githubusercontent.com/tldr-pages/tldr): tar, find, ncdu, distrobox, curl, wget, du, df, grep, sed, awk, dig, ping, ps, htop, tail, tmux, screen, cut, tr, sort, uniq, diff, rsync, rg, locate, less, head, wc, cat, ls, cd, mkdir, ln, chmod, chown, sudo, history, kill, pkill, pgrep, nohup, fd, gzip, zip, unzip, xz
- ShellCheck: github.com/koalaman/shellcheck and its wiki, SC2086
- explainshell.com (home page)
- Fedora/Red Hat: coreos.github.io/rpm-ostree/administrator-handbook/
- Bazzite docs: docs.bazzite.gg (home, Installing_and_Managing_Software, Updates_Rollbacks_and_Rebasing)
- distrobox.it; docs.flatpak.org/en/latest/using-flatpak.html; userbase.kde.org/Konsole
