# 📝 Todo Web App — Build Log & Learning Report

**Author:** Jack  
**Date:** 2025-09-16  
**Stack:** React + FastAPI + Postgres  
**Purpose:** Accessible, reproducible task manager with changelog discipline

---

## 🧱 Backend Overview

**Framework:** FastAPI  
**Database:** PostgreSQL 17  
**Driver:** psycopg2 with RealDictCursor

### Endpoints Implemented
- `GET /tasks` → Fetch all tasks
- `POST /tasks` → Add new task
- `PUT /tasks/{id}` → Update task completion
- `DELETE /tasks/{id}` → Remove task by ID

**CORS** enabled for frontend at `localhost:5173`

### Key Concepts
1. **RealDictCursor** returns rows as dictionaries, not tuples.
2. **RETURNING id** retrieves the inserted/updated row’s ID.
3. **CORS** allows frontend and backend to communicate across ports.

---

## 🎨 Frontend Overview

**Framework:** React (Vite)  
**State Management:** React hooks (no Redux)  
**Components:**
- `App.jsx`
- `NewTodoForm.jsx`
- `TodoList.jsx`
- `TodoItem.jsx`

LocalStorage removed. All state now synced with backend via `fetch()`.

### Key Concepts
4. `useEffect()` triggers backend fetch on mount.
5. `e.preventDefault()` prevents page reload on form submit.
6. `crypto.randomUUID()` replaced by Postgres auto-incremented IDs.

---

## 📚 Reproducibility Practices

- All changes logged in `CHANGELOG.md`
- Each backend endpoint validated with `curl` before frontend wiring
- Errors and fixes documented for future reference

### Key Concepts
7. Logging CLI errors prevents repetition and supports AI context.
8. `curl` validation isolates backend issues from frontend.
9. Changelog discipline supports learning, morale, and collaboration.

---

## 🧠 Deeper Concepts

### 10. PUT vs PATCH
- **PUT** replaces the entire resource.
- **PATCH** updates only specified fields.
- PUT used here for simplicity; PATCH may be added later.

### 11. ORM (SQLAlchemy)
- Maps tables to Python classes.
- Enables cleaner queries, schema validation, and relationships.
- Tradeoff: abstraction adds complexity and overhead.
- Raw SQL preferred here for clarity and reproducibility.

### 12. Environment Variables
- Extract secrets (e.g. DB password) from code.
- Use `os.environ["DB_PASS"]` in Python.
- Define values in `.env` or Docker container for portability.

---

## ✅ Next Steps

- Dockerize backend with `.env` support
- Add mobile responsiveness to React UI
- Add logging and error boundaries for robustness