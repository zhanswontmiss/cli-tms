# CLI Task Manager

A command-line Task Manager built with Python. It allows users to create, manage, organize, search, and track tasks through an interactive terminal interface.

## Features

- **Create Tasks** — Add tasks with a title, deadline, category, priority, and status.
- **Delete Tasks** — Remove tasks by their unique ID.
- **View Tasks** — Display all tasks or retrieve a specific task by ID.
- **Update Tasks** — Change task status, priority, and deadline.
- **Filter Tasks** — Filter tasks by status or priority.
- **Sort Tasks** — Organize tasks by their deadlines.
- **Search Tasks** — Find tasks by title using case-insensitive partial matching.
- **Data Persistence** — Automatically save and load tasks using JSON.
- **Input Validation** — Validate task information and prevent invalid data.

## Technologies

- Python
- JSON
- `unittest` — Python's built-in testing framework

## Project Structure

```text
cli-tms/
│
├── main.py
├── task.py
├── task_manager.py
├── search.py
│
├── test_task.py
├── test_task_manager.py
├── test_search.py
│
├── tasks.json
└── README.md
```

`tasks.json` is generated automatically when the application saves its data. It is excluded from version control.

## Getting Started

### Prerequisites

- Python 3.10 or newer

### Installation

Clone the repository:

```bash
git clone https://github.com/zhanswontmiss/cli-tms.git
```

Navigate to the project directory:

```bash
cd cli-tms
```

### Run the Application

```bash
python main.py
```

Follow the interactive menu to manage your tasks.

## Running Tests

Run the complete test suite:

```bash
python -m unittest discover -v
```

The project uses Python's built-in `unittest` framework to test task validation, task management operations, and search functionality.

## Data Storage

Tasks are stored locally in `tasks.json` using JSON serialization. The application automatically loads saved tasks when it starts and saves changes when tasks are modified.

## Future Improvements

- Add task editing functionality for titles and categories.
- Introduce task statistics and progress tracking.
- Add support for recurring tasks.
- Implement more advanced search and filtering options.

## License

This project is currently available for educational and personal use.