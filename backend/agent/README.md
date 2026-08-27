# LOTTO‑AICE — Backend Agent
Adaptive Institutional Collaborative Engine (AICE)  
LAST OF TRUE TORONTO LTD.

---

## 🚀 Overview
This directory contains the executable backend for LOTTO‑AICE — the lightweight reasoning agent powering LAST OF TRUE TORONTO LTD.'s institutional intelligence system.

It includes:
- The agent runtime
- The reasoning loop
- The tool router
- The memory modules
- The artifact generator
- The container build files

This backend is designed for rapid iteration, partner demos, and hackathon submission.

---

## 🧠 Architecture

backend/
  agent/
    aice_agent.py
    reasoning_loop.py
    tools_router.py
    task_planner.py
    notes_store.py
    session_memory.py
    project_memory.py
    docs_template.py
    requirements.txt
    Dockerfile

### Component Summary
- **aice_agent.py** — Main agent wrapper  
- **reasoning_loop.py** — Intent → plan → tool → synthesis pipeline  
- **tools_router.py** — Minimal tool routing logic  
- **task_planner.py** — Structured plan generation  
- **notes_store.py** — Notes + memory write operations  
- **session_memory.py** — Ephemeral session memory  
- **project_memory.py** — Persistent project memory  
- **docs_template.py** — Artifact generation templates  
- **requirements.txt** — Python dependencies  
- **Dockerfile** — Container build for Cloud Run / local dev  

---

## ⚙️ Local Development

### Run with Docker Compose (recommended)
From repo root:

This builds and runs the LOTTO‑AICE backend agent container.

### Run directly with Python


---

## 🧪 Continuous Integration (CI)
The repo includes a lightweight CI workflow:


It performs:
- Python setup  
- Requirements installation  
- Smoke import test  
- Basic module validation  

Ensures the backend agent always imports cleanly.

---

## 📦 Deployment (Cloud Run)

### Build


### Deploy


---

## 🎥 Demo Script
See `DEMO.md` for the 60–90s partner demo.

Covers:
- One-line value prop  
- Local run  
- Live agent interaction  
- Next-step integration plan  

---

## 🗂 Archive Notice
The original `/aice` directory has been archived under:


This preserves the full historical tree while the backend agent moves forward under the new structure.

---

## 🏢 About LAST OF TRUE TORONTO LTD.
A world-first institutional design company building:
- myth‑tech systems  
- adaptive intelligence engines  
- founder‑grade operational frameworks  
- institutional cosmology  

AICE is its first public agent.

---

## 📬 Contact
**SHELL — Founder & CEO**  
LAST OF TRUE TORONTO LTD.
