# 🧰 Bench CLI Cheat Sheet

## 🎯 Bench Init & Apps

| Command | Purpose / Example |
|---------|-------------------|
| `bench init <bench>` | Create a new bench folder |
| `bench get-app <name> <repo>` | Get an app from GitHub |
| `bench new-app <name>` | Create boilerplate app |
| `bench remove-app <app>` | Remove app & rebuild |
| `bench build` | Build JS/CSS assets |
| `bench watch` | Watch & auto-build assets |
| `bench update` | Pull, migrate, rebuild |
| `bench restart` | Restart background services |
| `bench migrate-env python3.x` | Change Python version |
| `bench config <key> <value>` | Change bench config |

---

## 🌐 Site Management

| Command | Purpose / Example |
|---------|-------------------|
| `bench new-site <site>` | Create a site |
| `bench use <site>` | Set default site |
| `bench drop-site <site>` | Delete site |
| `bench reinstall` | Reinstall site |
| `bench restore <backup.sql>` | Restore from SQL |
| `bench backup` | Backup DB & files |

---

## 🔷 Apps in Site

| Command | Purpose / Example |
|---------|-------------------|
| `bench install-app <app>` | Install app on site |
| `bench uninstall-app <app>` | Remove app |
| `bench list-apps` | List installed apps |
| `bench version` | Show versions |

---

## 👨‍💻 Development

| Command | Purpose / Example |
|---------|-------------------|
| `bench console` | Python REPL with site context |
| `bench execute <path>` | Run Python function |
| `bench migrate` | DB migrate & sync |
| `bench reset-perms` | Reset DocType permissions |
| `bench reload-doctype <dt>` | Reload schema |
| `bench run-tests` | Run unit tests |
| `bench build-search-index` | Rebuild search index |

---

## 🧹 Cache & Maintenance

| Command | Purpose / Example |
|---------|-------------------|
| `bench clear-cache` | Clear cache |
| `bench clear-website-cache` | Clear website cache |
| `bench set-maintenance-mode on/off` | Maintenance mode |

---

## ⏱️ Scheduler & Jobs

| Command | Purpose / Example |
|---------|-------------------|
| `bench schedule` | Start scheduler |
| `bench scheduler resume/pause` | Toggle scheduler |
| `bench show-pending-jobs` | List jobs |
| `bench purge-jobs` | Clear jobs |

---

## 🗄️ Database

| Command | Purpose / Example |
|---------|-------------------|
| `bench db-console` | DB shell |
| `bench mariadb` | DB shell (MariaDB) |
| `bench describe-database-table <table>` | Table info |

---

## 🌍 Web & Browser

| Command | Purpose / Example |
|---------|-------------------|
| `bench serve` | Dev server |
| `bench browse` | Open in browser |
| `bench ngrok` | Expose site via ngrok |

---

## 🛠️ Utilities & Admin

| Command | Purpose / Example |
|---------|-------------------|
| `bench doctor` | Diagnose workers & scheduler |
| `bench destroy-all-sessions` | Logout all users |
| `bench set-admin-password <pw>` | Set admin password |
| `bench set-password <user> <pw>` | Set user password |

---

## 🌏 Translation & L10n

| Command | Purpose / Example |
|---------|-------------------|
| `bench build-message-files` | Build translations |
| `bench get-untranslated` | Find untranslated strings |
| `bench update-translations` | Update translations |

---

## 🖥️ Workers & Background

| Command | Purpose / Example |
|---------|-------------------|
| `bench worker` | Start worker |
| `bench worker-pool` | Start worker pool |

---

## 👇 Notes

- Always run from **bench folder**
- Use `--site <site>` if multiple sites:  
  Example:  
  ```bash
  bench --site mysite.local clear-cache
