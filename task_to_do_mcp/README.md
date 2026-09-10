# Task / To-Do Manager — MCP Server

A beginner-friendly Model Context Protocol (MCP) server built according to the **MCP Lab Activity — Beginner Edition**.

The lab asks for:
- at least 5 tools
- simple storage using a list/dictionary or one JSON file
- clear error handling
- a README with setup and examples
- an optional read-only resource
- stdio transport

This project implements **5 tools** and **1 bonus resource**.

## Project Structure

```text
task_to_do_mcp/
├── server.py
├── requirements.txt
├── README.md
└── tasks.json
```

## Tools

| Tool | Purpose | Inputs |
|---|---|---|
| `add_task` | Creates a new task | `title`, `description` |
| `list_tasks` | Lists all tasks | none |
| `get_task` | Gets one task | `task_id` |
| `complete_task` | Marks a task completed | `task_id` |
| `delete_task` | Deletes a task | `task_id` |

### Bonus Resource

`tasks://pending`

This is read-only and shows the current pending tasks. It is a resource rather than a tool because it only exposes information and does not perform an action.

## Requirements

- Python 3.10+
- MCP Python SDK
- MCP Inspector

## Installation — Windows

Open PowerShell in the project folder:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

If PowerShell blocks activation, you can still install/run using:

```powershell
python -m pip install -r requirements.txt
python server.py
```

## Run the Server

```powershell
python server.py
```

The server uses **stdio transport**, as required by the beginner lab.

For MCP Inspector, use the command:

```text
python server.py
```

and connect using the Inspector's STDIO option.

## Example Calls

### 1. Add a task

```text
add_task
title = "Complete MCP lab"
description = "Finish the Task Manager project"
```

Expected result:

```text
Task added successfully: #1 - Complete MCP lab
```

### 2. List tasks

```text
list_tasks
```

Example result:

```text
#1 [Pending] Complete MCP lab — Finish the Task Manager project
```

### 3. Get a task

```text
get_task
task_id = 1
```

### 4. Complete a task

```text
complete_task
task_id = 1
```

Expected result:

```text
Task #1 marked as completed.
```

### 5. Delete a task

```text
delete_task
task_id = 1
```

## Error Handling

The server does not intentionally crash for common bad input.

Examples:

- Empty title → `Error: title is required and cannot be empty.`
- Invalid ID → `Error: task_id must be a positive integer.`
- Missing task → `Error: task #X was not found.`

## Storage

Tasks are stored in one local file:

```text
tasks.json
```

No database, cloud service, or external storage is used, matching the lab rules.

## Suggested 5-Minute Demo

1. Start the MCP server.
2. Open MCP Inspector and connect through STDIO.
3. Show the five tools.
4. Call `add_task`.
5. Call `list_tasks`.
6. Call `complete_task`.
7. Call `get_task`.
8. Open the `tasks://pending` resource.
9. Call `delete_task`.
10. Demonstrate one invalid input and show the friendly error.

## Viva Preparation

**What problem does MCP solve?**  
MCP provides a standard way for an AI assistant/client to communicate with outside programs and data.

**What are the two sides?**  
The MCP client calls the MCP server. The server provides tools and resources.

**What is a tool?**  
A tool is an action the client can trigger, such as `add_task`.

**Tool vs resource?**  
A tool performs an action. A resource provides read-only information.

**What transport did you use?**  
STDIO, because the lab specifically uses the simplest local transport.

**How is data stored?**  
In a local `tasks.json` file.

**What happens with bad input?**  
The tool returns a clear error message instead of intentionally crashing the server.

## Lab Alignment

This project follows the project option listed in Section 6 of the supplied lab:

`Task / To-Do Manager`

Required tools:

`add_task, list_tasks, get_task, complete_task, delete_task`

Bonus resource:

`tasks://pending`

The supplied lab also requires a minimum of five tools, simple storage, error handling, README documentation, and a live demo. This project includes all of these elements.
