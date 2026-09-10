from mcp.server.fastmcp import FastMCP
import json
import os
from typing import Optional

mcp = FastMCP("Task To-Do Manager")

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def clean_text(value: str, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Error: {field} is required and cannot be empty.")
    return value.strip()


@mcp.tool()
def add_task(title: str, description: str = "") -> str:
    """Create a new task with a title and optional description."""
    try:
        title = clean_text(title, "title")
        if not isinstance(description, str):
            return "Error: description must be text."
        tasks = load_tasks()
        next_id = max((task["id"] for task in tasks), default=0) + 1
        task = {
            "id": next_id,
            "title": title,
            "description": description.strip(),
            "completed": False
        }
        tasks.append(task)
        save_tasks(tasks)
        return f"Task added successfully: #{next_id} - {title}"
    except ValueError as e:
        return str(e)
    except OSError:
        return "Error: could not save the task."


@mcp.tool()
def list_tasks() -> str:
    """List all tasks with their current completion status."""
    tasks = load_tasks()
    if not tasks:
        return "No tasks found."
    lines = []
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        lines.append(
            f'#{task["id"]} [{status}] {task["title"]}'
            + (f' — {task["description"]}' if task["description"] else "")
        )
    return "\n".join(lines)


@mcp.tool()
def get_task(task_id: int) -> str:
    """Get one task by its numeric ID."""
    if not isinstance(task_id, int) or isinstance(task_id, bool) or task_id <= 0:
        return "Error: task_id must be a positive integer."
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return json.dumps(task, indent=2, ensure_ascii=False)
    return f"Error: task #{task_id} was not found."


@mcp.tool()
def complete_task(task_id: int) -> str:
    """Mark a task as completed by its numeric ID."""
    if not isinstance(task_id, int) or isinstance(task_id, bool) or task_id <= 0:
        return "Error: task_id must be a positive integer."
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                return f"Task #{task_id} is already completed."
            task["completed"] = True
            save_tasks(tasks)
            return f"Task #{task_id} marked as completed."
    return f"Error: task #{task_id} was not found."


@mcp.tool()
def delete_task(task_id: int) -> str:
    """Delete a task by its numeric ID."""
    if not isinstance(task_id, int) or isinstance(task_id, bool) or task_id <= 0:
        return "Error: task_id must be a positive integer."
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(index)
            save_tasks(tasks)
            return f'Task #{task_id} deleted: {deleted["title"]}'
    return f"Error: task #{task_id} was not found."


@mcp.resource("tasks://pending")
def pending_tasks() -> str:
    """Read-only resource containing all pending tasks."""
    tasks = load_tasks()
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        return "No pending tasks."
    return json.dumps(pending, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    mcp.run(transport="stdio")
