---
name: nextcloud-specialist
description: Use when helping a non-programmer run, secure, back up, update or troubleshoot a personal Nextcloud (likely Docker on Unraid) with the Linux desktop client and ONLYOFFICE.
---

# Nextcloud specialist

## Labels
- VERIFIED (source) = read in a page I fetched, listed under Sources.
- COMMUNITY = widely repeated practice, not verified in a fetched page.
- UNVERIFIED = from memory; check before relying on it.
- docs.nextcloud.com blocked my fetcher (robots), so doc facts below come from the same docs' public source files on GitHub.

## How to work with the reader
- Assume the reader is not a programmer. Plain words first, then the exact command.
- One change at a time. Ask the reader to confirm the result before the next step.
- Before any advice, ask which install type they have (see next section).
- Back up before risky steps; never ask the reader to paste passwords, keys or their public IP; the desktop client only connects out.

## Which install type does the reader have?
- Ask the reader to run on the Unraid terminal: `docker ps`. Then read the container names.
- `nextcloud-aio-mastercontainer` and other `nextcloud-aio-` containers = AIO. VERIFIED (AIO readme).
- One `nextcloud` container from the Unraid Community Apps template plus a separate database container = Unraid template. UNVERIFIED.
- Official image `nextcloud` with /var/www/html volumes = official Docker. VERIFIED (docker README).
- Do not give paths or commands until the type is known.

## Running occ (Nextcloud's command tool)
- AIO: `sudo docker exec --user www-data -it nextcloud-aio-nextcloud php occ <command>`. VERIFIED (AIO readme).
- Official Docker: `docker exec -it --user www-data <container> php occ <command>`. VERIFIED (docker README). Alpine images use user 82 instead of 33. VERIFIED.

## HTTPS, reverse proxy, trusted domains
- Always HTTPS, never plain HTTP in production. VERIFIED (hardening docs).
- HSTS header `Strict-Transport-Security: max-age=15552000; includeSubDomains`; drop includeSubDomains if any subdomain lacks HTTPS. VERIFIED (hardening docs).
- `trusted_domains` = hostnames allowed to log in; wildcards and ports allowed. VERIFIED (config sample).
- Behind a proxy set `trusted_proxies` to the proxy's address only. VERIFIED (proxy docs).
- `overwriteprotocol` = `https` when the proxy ends TLS and detection fails. VERIFIED (proxy docs).
- Wrong `forwarded_for_headers` can let clients fake their IP. VERIFIED.
- AIO behind a proxy: pick APACHE_PORT (docs example 11000), forward Host, X-Forwarded-Host, X-Forwarded-Proto=https, X-Forwarded-For, X-Real-IP, plus WebSocket headers. VERIFIED (AIO reverse-proxy doc).
- AIO: open the admin page by IP on 8080, not by domain (HSTS can lock you out). VERIFIED.

## Background jobs (cron)
- Modes: AJAX (default, weakest), Webcron, Cron. Cron is recommended. VERIFIED (background jobs doc).
- Cron line, every 5 minutes: `*/5 * * * * php -f /var/www/nextcloud/cron.php`. VERIFIED.
- `maintenance_window_start` (UTC hour) pushes heavy jobs into the night; default 100 = off. VERIFIED.
  - `occ config:system:set maintenance_window_start --type=integer --value=1`. VERIFIED.

## Caching, PHP, database
- APCu for local cache; Redis for file locking. VERIFIED (caching doc).
- Config: `memcache.local` = `\OC\Memcache\APCu`; `memcache.distributed` and `memcache.locking` = `\OC\Memcache\Redis`; plus a `redis` block (host, port, optional password). VERIFIED.
- APCu default `apc.shm_size` 32M is often low; docs suggest 128M. VERIFIED.
- PHP `memory_limit` at least 512MB. VERIFIED (php config doc).
- OPcache: `opcache.revalidate_freq=60`, `opcache.save_comments=1` (required). VERIFIED (tuning doc).
- Recommended databases: MariaDB 11.8 or PostgreSQL 18 (per current requirements page); SQLite only for tests. VERIFIED.

## Storage and external storage
- Without push notifications, run `files_external:scan` from cron about every 15 minutes. VERIFIED.

## Linux sync client
- Flatpak (Flathub `com.nextcloud.desktopclient.nextcloud`), AppImage, distro package. UNVERIFIED; check the name on Flathub before giving it.
- Use selective sync to keep big folders (for example stems, bounces, samples) off the desktop. COMMUNITY.
- Music projects: do not sync caches and freeze files (`*.asd`, `Bounced Files`, `Backup`); hands off live DAW project folders on two PCs at once. COMMUNITY.
- After a restore, `occ maintenance:data-fingerprint` makes clients show conflict dialogs. VERIFIED (restore doc).

## Passwords, app passwords, 2FA
- TOTP 2FA app is off by default; enable in Apps. Any RFC 6238 app works. VERIFIED (2FA doc).
- Admin can enforce 2FA in Administration, Security. VERIFIED.
- Locked out: `occ twofactorauth:disable <uid> <provider_id>`; check with `occ twofactorauth:state <uid>`. VERIFIED.
- Sharing: enforce link passwords and expiry dates; leave "Allow public uploads" off. VERIFIED (sharing doc).

## Server-side encryption caveats
- Encrypts only file contents; filenames, folders, thumbnails, search index stay readable. VERIFIED (encryption doc).
- Does not protect against a compromised server or admin. VERIFIED.
- Lose the keys or instance secret = permanent data loss. VERIFIED.

## Backups and restore
- Back up before every update. VERIFIED.
- Bare/official Docker: maintenance mode on, copy config, data, custom apps, theme; dump the database; maintenance mode off. VERIFIED (backup doc).
- MariaDB dump: `mariadb-dump --single-transaction` ; PostgreSQL: `pg_dump`. VERIFIED.
- Restore: copy folders back (docs use `rsync -Aax`), drop and recreate the database, import the dump. VERIFIED (restore doc).
- Then, only if the backup is older than client data: `occ maintenance:data-fingerprint`, then `occ files:scan`. VERIFIED.
- AIO: built-in BorgBackup, with optional daily backups, from the AIO page. VERIFIED.

## Updating safely
- One major version at a time; never skip. VERIFIED (upgrade doc and docker README).
- Update to the latest point release of your major, then the next major. VERIFIED.
- After a major upgrade run cron.php two or three times before the next major. VERIFIED.
- Disable third-party apps before upgrading, re-enable after. VERIFIED.
- Then: `occ db:add-missing-columns`, `occ db:add-missing-indices`, `occ db:add-missing-primary-keys` (`--dry-run` shows SQL). VERIFIED.
- AIO: stop containers, then "Start and update containers"; update the mastercontainer separately. VERIFIED.
- Official Docker: pull the new image tag; the container migrates on start. VERIFIED.
- Current release: "Hub 26 Spring" announced 2026-06-09; the server major number was not stated in what I fetched. VERIFIED (help.nextcloud.com post), number UNVERIFIED. Check Settings, Overview before advising.

## occ cheat sheet (prefix with the wrapper for your install type)
- `occ status`. VERIFIED.
- `occ twofactorauth:disable <uid> <provider>`. VERIFIED.
- `occ user:resetpassword <uid>`. UNVERIFIED.

## Logs
- File: `data/nextcloud.log`; or Administration, Logging. VERIFIED.
- Ask for the full raw log line, with any IPs and names removed.

## Hardening checklist
- HTTPS plus HSTS. VERIFIED.
- Data directory outside the web root. VERIFIED.
- `debug` false. VERIFIED.
- Public shares: password and expiry. VERIFIED.
- External scan at scan.nextcloud.com: I could not fetch it. UNVERIFIED. It tests a public address, so ask before submitting a domain.

## ONLYOFFICE pitfalls
- Document Server address must be reachable from the reader's browser AND from Nextcloud. VERIFIED (connector readme).
- Document Server must reach Nextcloud back (StorageUrl); use `DocumentServerInternalUrl` when the public address will not work from inside. VERIFIED.
- JWT is on by default since connector 7.2; the same secret must be set on both sides. VERIFIED.
- Test with `occ onlyoffice:documentserver --check`. VERIFIED.
- Self-signed certs: "disable certificate verification" is temporary only; get a real certificate. VERIFIED.
- "Local addresses not allowed" errors may need `allow_local_remote_servers` = true in config.php. COMMUNITY (readme did not mention it; default is false per config sample, VERIFIED).

## Troubleshooting tree (ask one question at a time)
- "Access through untrusted domain":
  - Which URL is being typed? Is it in `trusted_domains`? Fix with the env var or config. VERIFIED.
- 502 Bad Gateway:
  - Is PHP-FPM or the Nextcloud container running (`docker ps`)? COMMUNITY.
  - nginx upstream address must match PHP-FPM listen (socket vs port). VERIFIED.
  - AIO: proxy port must equal APACHE_PORT. VERIFIED.
- Slow:
  - Redis plus APCu on? PHP-FPM children too few? Cron really running? Previews heavy? VERIFIED (tuning doc).
  - Not on SQLite. VERIFIED.
- Sync stuck:
  - Client log first; server log second. COMMUNITY.
  - Did anyone edit the data folder by hand? Run `files:scan`. VERIFIED.
  - Proxy upload size limits or timeouts. VERIFIED.
  - Last resort: pause, remove one folder from sync, re-add. COMMUNITY.
- "File is locked":
  - Check Redis is up (locking uses it). VERIFIED.
  - Stale locks release after interrupted transactions; docs give no manual clear steps. VERIFIED (absence).
  - Close the file in other apps/devices, wait, retry. COMMUNITY.

## Sources (fetched)
- https://raw.githubusercontent.com/nextcloud/all-in-one/main/readme.md
- https://raw.githubusercontent.com/nextcloud/all-in-one/main/reverse-proxy.md
- https://raw.githubusercontent.com/nextcloud/docker/master/README.md
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/installation/harden_server.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_server/reverse_proxy_configuration.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_server/background_jobs_configuration.rst
- https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/caching_configuration.html
- https://docs.nextcloud.com/server/latest/admin_manual/occ_command.html
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/maintenance/backup.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/maintenance/restore.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/maintenance/upgrade.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/installation/server_tuning.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/installation/system_requirements.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/installation/php_configuration.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/installation/nginx.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_files/encryption_configuration.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_files/external_storage_configuration_gui.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_files/files_locking_transactional.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_files/big_file_upload_configuration.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_files/file_sharing_configuration.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_server/config_sample_php_parameters.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/configuration_user/two_factor-auth.rst
- https://raw.githubusercontent.com/nextcloud/documentation/master/admin_manual/issues/general_troubleshooting.rst
- https://raw.githubusercontent.com/ONLYOFFICE/onlyoffice-nextcloud/master/README.md
- https://raw.githubusercontent.com/nextcloud/desktop/master/README.md
- https://help.nextcloud.com/t/nextcloud-hub-26-spring-built-together-designed-for-the-future/245611.md