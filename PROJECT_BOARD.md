
# 🗺️ MindMeld GitHub Project Board Roadmap

This file tracks the current status and roadmap for the MindMeld Modular LLM Backend, formatted for GitHub Projects (classic or beta boards). Use this to create GitHub issues or cards, and move items between `Backlog`, `Now`, `Next`, and `Done`.

---

## ✅ Columns for GitHub Project Board

- **Backlog** — Features/infra you plan to build later
- **Now** — What you're actively working on
- **Next** — What comes after current active work
- **Done** — Completed and committed tasks

---

## 🧱 Project Board Items (Copy into GitHub Project)

### Backlog
- Add Prometheus metrics for `/chat` and `/analyze`
- Build `/prompt/advanced` endpoint (template-based prompts)
- Scaffold `/convert` file upload + PDF/Text extraction
- Implement `/tts` and `/stt` with OpenAI Whisper + TTS
- Build embedding drift detector (Phase 2+)
- Add `/task/execute` for agent orchestration (Phase 3)
- Add rate-limiting middleware

### Now
- [x] Scaffold `/analyze` route (model, service, route, test)
- [ ] Add structured logging (loguru + request ID middleware)
- [ ] Define custom service errors and global exception handlers

### Next
- [ ] Refactor Claude-generated files into folders if flat
- [ ] Push repo to GitHub with updated README + roadmap
- [ ] Add test coverage summary to `/tests/`
- [ ] Lock Claude into scoped “active task” mode using `claude-tasks.md`

### Done
- [x] Clone and set up repo structure
- [x] Create `.venv` and activate with Python 3.10.13
- [x] Launch FastAPI `/health` endpoint
- [x] Configure `.env` and `core/config.py`
- [x] Scaffold `/chat` route with OpenAI GPT
- [x] Create project instructions and load into Claude
- [x] Generate `claude-project-instructions.md` and `project-info.md`

---

## 📌 Usage

- Keep this file in `/docs/project-roadmap.md` or `/PROJECT_BOARD.md`
- Link it in your GitHub project as a board reference
- Add checkboxes to issues as needed for task breakdowns

---
