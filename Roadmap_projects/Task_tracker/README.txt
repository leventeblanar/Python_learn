Roadmap.sh - TASK TRACKER Project

Project UL: https://roadmap.sh/projects/task-tracker


This is a simple JSON-based Python program for keeping track of tasks (to-do list).
All tasks are stored in a file named `task_db.json`.

## Features

* **Create new task** (1)
  Add a short description; the program automatically generates an ID and timestamps.

* **Modify task** (2)
  Update the description or set the status to *In progress*.

* **Mark task as done** (3)
  Change the status of a task to *Done*.

* **Delete task** (4)
  Permanently remove a task by its ID.

* **List tasks**

  * (5) Show all tasks
  * (6) Show only completed (*Done*) tasks
  * (7) Show only not completed tasks (*New* and *In progress*)
  * (8) Show only tasks in progress

## Status values

* `New` – newly created task
* `In progress` – task currently being worked on
* `Done` – finished task

## Usage

Run the program from the command line:

```bash
python task_tracker.py
```

The application provides an interactive menu.
Use numbers (1–8) to select actions, or type `exit` to quit.

## Data storage

All data is stored in `task_db.json` in the project folder.
The file is a simple JSON list; each task contains the following fields:

```json
{
    "id": 1,
    "description": "Example task",
    "status": "New",
    "created_at": "2025-10-01 12:00:00",
    "updated_at": "2025-10-01 12:00:00"
}
```

---

Do you want me to also add a **short example session** (like creating a task, then marking it as done) to make the README more beginner-friendly?
