
File structure:
To Do List/
├── node_modules/                  # Project dependencies (auto-managed)
├── src/                           # Source code
│   ├── components/                # Modular React components
│   │   ├── NewTodoForm.jsx        # Form to add new todo items
│   │   ├── TodoItem.jsx           # Renders individual todo items
│   │   ├── TodoList.jsx           # Maps and renders list of todos
│   │   └── UseLocalStorage.jsx    # Custom hook for localStorage sync
│   ├── App.jsx                    # Root component managing state and logic
│   ├── main.jsx                   # React entry point, mounts App
│   └── styles.css                 # Global styling and layout
├── index.html                     # HTML shell, links to main.jsx
├── package.json                   # Project metadata and dependencies
├── package-lock.json              # Exact dependency tree snapshot
├── vite.config.js                 # Vite build tool configuration
├── eslint.config.js              # ESLint rules for code linting
├── .gitignore                     # Git version control exclusions
├── README.md                      # Project documentation
└── CHANGELOG.md                   # Change tracking (now initialized)
└──requirements.txt                #track/install dependencies


2025-09-15 Created React/Vite frontend with localStorage-based todo list. Added components: App.jsx, NewTodoForm.jsx, TodoList.jsx, TodoItem.jsx, useLocalStorage.jsx. Mounted App via main.jsx. Added styles.css for layout and interactive styling. Linked entry point in index.html.

2025-09-15 Installed FastAPI, Uvicorn, and psycopg2 for backend API and Postgres connectivity.

2025-09-15 Created CHANGELOG.md to track project changes and enforce reproducibility.

2025-09-15 Added requirements.txt to define backend Python dependencies.

2025-09-15 Added FastAPI backend file main.py with GET /tasks endpoint to fetch todos from Postgres.

2025-09-15 Opened SystemPropertiesAdvanced via elevated Command Prompt to enable PATH editing.

2025-09-15 Attempted Python install to C:\Python313; manually moved folder caused runtime corruption.

2025-09-15 Cleaned system PATH and deleted all Python-related folders from C:\ and Program Files.

2025-09-15 Removed broken registry keys from HKEY_LOCAL_MACHINE and HKEY_CURRENT_USER to eliminate Python traces.

2025-09-15 Reinstalled Python using official installer with correct PATH and environment settings. Verified install and reinstalled backend dependencies. This fixed pip --version error. Issue was python was not in program files and path.

2025-09-15 Resolved uvicorn CLI issue by invoking FastAPI server via python -m uvicorn from correct project root.

2025-09-15 Validated GET /tasks endpoint from FastAPI backend. Confirmed Postgres connectivity and JSON response.

2025-09-15 Added POST /tasks endpoint to insert new todos into Postgres. Defined input schema and response format.


2025-09-15 Scaffolded POST /tasks endpoint with input schema; insertion logic pending.

2025-09-16 Validated POST /tasks accepts JSON payload; response structure confirmed. Insert logic still placeholder.

2025-09-16 Implemented actual insert logic for POST /tasks using psycopg2 and Pydantic validation.

2025-09-16 Added DELETE /tasks/{id} endpoint to remove tasks from Postgres by ID.

2025-09-16 Added PUT /tasks/{id} endpoint to update task completion status in Postgres.

2025-09-16 Rewired App.jsx to sync todos with FastAPI backend via fetch; removed useLocalStorage.

2025-09-16 Updated NewTodoForm.jsx to delegate task creation to backend via App.jsx POST logic.

2025-09-16 Enabled CORS in FastAPI to allow frontend requests from localhost:5173.





