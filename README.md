# Exercice1-Diaw-Ndeye

## Description

This is a simple Todo application backend built with Python using the built-in `http.server` module. It provides a RESTful API for managing todo tasks.

## Features

- Get all todos
- Create a new todo
- Update a todo (mark as completed)
- Delete a todo

## API Endpoints

### GET /todos

Retrieves all todo tasks.

**Response:**

```json
{
  "status": 200,
  "data": [
    {
      "id": 1,
      "title": "Sample Task",
      "done": false
    }
  ]
}
```

### POST /todos

Creates a new todo task.

**Request Body:**

```json
{
  "title": "New Task Title"
}
```

**Response:**

```json
{
  "status": 201,
  "data": {
    "id": 1,
    "title": "New Task Title",
    "done": false
  }
}
```

### PATCH /todos/{id}

Updates a todo task (marks as completed or not).

**Request Body:**

```json
{
  "done": true
}
```

**Response:**

```json
{
  "status": 200,
  "data": {
    "id": 1,
    "title": "New Task Title",
    "done": true
  }
}
```

### DELETE /todos/{id}

Deletes a todo task.

**Response:**

```json
{
  "status": 200,
  "message": "Tâche supprimée",
  "data": {
    "id": 1,
    "title": "New Task Title",
    "done": false
  }
}
```

## Project Structure

```
.
├── Controller/
│   └── TodoController.py
├── Model/
│   └── TodoModel.py
├── Routes/
│   └── TodoRoutes.py
├── server.py
├── README.md
└── .gitignore
```

## Installation and Running

1. Ensure you have Python 3 installed.
2. Clone or download the project.
3. Run the server:
   ```bash
   python server.py
   ```
4. The server will start on `http://localhost:5000`.

## Usage

Use tools like curl, Postman, or any HTTP client to interact with the API endpoints.

Example curl commands:

- Get all todos: `curl http://localhost:5000/todos`
- Create a todo: `curl -X POST -H "Content-Type: application/json" -d '{"title":"My Task"}' http://localhost:5000/todos`
- Update a todo: `curl -X PATCH -H "Content-Type: application/json" -d '{"done":true}' http://localhost:5000/todos/1`
- Delete a todo: `curl -X DELETE http://localhost:5000/todos/1`
