# To-Do List REST API

## Project Description

This project is a To-Do List REST API developed using **Python** and **FastAPI**. It performs CRUD (Create, Read, Update, Delete) operations on tasks. The application stores data in a Python list instead of a database.

## Features

- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Delete a task
- Automatic API documentation with Swagger UI

## Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

```
Todo Project/
│
├── app/
│   └── main.py
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project Folder

```bash
cd Todo-Project
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m uvicorn app.main:app --reload
```

The application will start on:

```
http://127.0.0.1:8000
```

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Create a Task

**POST**

```
/todos
```

Request Body

```json
{
    "title": "Finish Python Assignment"
}
```

### Get All Tasks

**GET**

```
/todos
```

### Get Task by ID

**GET**

```
/todos/{id}
```

Example

```
/todos/1
```

### Update Task

**PUT**

```
/todos/{id}
```

Request Body

```json
{
    "title": "Complete FastAPI Assignment",
    "completed": true
}
```

### Delete Task

**DELETE**

```
/todos/{id}
```

Example

```
/todos/1
```

## Sample Response

```json
{
    "id": 1,
    "title": "Finish Python Assignment",
    "completed": false
}
```

## Testing

The API can be tested using:

- Swagger UI
- Postman

## Learning Outcomes

- Build REST APIs using FastAPI
- Implement CRUD operations
- Use Pydantic for request validation
- Handle HTTP methods (GET, POST, PUT, DELETE)
- Store data in a Python list
- Test APIs using Swagger UI and Postman

## Author

**Sameer Malik**

BS Computer Science

Bahria University Lahore Campus
