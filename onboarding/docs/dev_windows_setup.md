# 🛠️ Barkibu Local Dev Setup & Debug Log

**Author:** Valentin Costea
**Date Started:** May 26, 2025
**Environment:** Windows 11, Docker Desktop, Git Bash / PowerShell

---

## ✅ Goal

Set up the full Barkibu codebase locally and get all services running in Docker: backend, frontend, Redis, PostgreSQL.

---

## 🔍 Initial Setup Steps

1. **Cloned project** into structured workspace:

   ```
   ~/dev/barkibu/claim_automation
   ```

2. **Set up SSH with GitHub** to avoid HTTPS token friction.

3. **Switched to a personal branch** for isolated setup/debug:

   ```bash
   git checkout -b valentin/local-setup
   ```

4. **Created a `.env` file** from example:

   ```bash
   cp backend/.env.example backend/.env
   ```

5. **Installed Docker Desktop**, enabled WSL2 integration, and verified Docker CLI.

---

## 🧨 Issues Encountered & Fixes

### ❌ Mac Symlink to `frontend` Broke on Windows

* `backend/frontend` was a **macOS-style symlink**
* On Windows, Docker couldn't copy to it → caused:

  ```
  mkdir /app/backend/frontend: not a directory
  ```

**Fix:**

* Deleted the symlink
* Created a real placeholder folder:

  ```bash
  mkdir backend/frontend
  ```

---

### ❌ Docker Compose All-at-Once Startup Was Too Noisy

* `docker-compose up` made debugging errors difficult

**Fix (via TL advice):** Started services individually:

```bash
docker-compose up -d redis postgres   # run core dependencies
docker-compose up web                 # run backend
docker-compose up frontend            # run frontend
```

---

### ❌ Google Cloud / Vertex AI Auth Failure

* Runtime crash:

  ```
  google.auth.exceptions.GoogleAuthError: Unable to find your project.
  ```
* Caused by missing or broken `credentials.json`

**Workaround:** Contacted team lead to request access and unblock initialization.

---

## ✅ Current State

* Migrations run successfully
* Redis, Postgres, Backend, and Frontend are all up
* Manual static build of frontend worked
* Docker config is now Windows-friendly

---

## 📌 Next Steps

* Attend app demo with tech lead
* Clarify system architecture and data flow
* Get first dev task assigned
* Propose a platform-safe solution to replace symlink usage

---

## 💬 Notes

This log is part of my personal onboarding progress. It's also useful for knowledge sharing, team documentation, and feedback.

