# The Scrumfather Documentation

## Overview
The Scrumfather is a backend API for managing users and projects, supporting user authentication and project CRUD operations. It is designed for productivity and personal project management.

## Technology Stack
- **Python 3**
- **FastAPI** (web framework)
- **Poetry** (dependency management)
- **SQLite** (default database)
- **Docker** (optional, for containerized deployment)

## Getting Started

### Prerequisites
- Python 3.8+
- Poetry

### Installation
```bash
poetry install
```

### Running the Application
```bash
poetry run python main.py
```
Or with Docker:
```bash
docker-compose up --build
```

## Authentication

### User Registration
Registers a new user.

```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
-H "Content-Type: application/json" \
-d '{
  "username": "new_user",
  "password": "secure_password"
}'
```

### User Login
Logs in and retrieves a JWT token.

```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{
  "username": "new_user",
  "password": "secure_password"
}'
```

**Response Example:**
```json
{
  "access_token": "your_jwt_token_here",
  "token_type": "bearer"
}
```

## Project Management API

### Create a Project
```bash
curl -X POST "http://127.0.0.1:8000/projects/create" \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{
  "name": "My New Project",
  "idea": "An app to manage personal finances"
}'
```

### Get All Projects
```bash
curl -X GET "http://127.0.0.1:8000/projects" \
-H "Authorization: Bearer <your_token>"
```

### Get Project Details
```bash
curl -X GET "http://127.0.0.1:8000/projects/<project_id>" \
-H "Authorization: Bearer <your_token>"
```
Replace `<project_id>` with the actual project ID.

### Delete a Project
```bash
curl -X DELETE "http://127.0.0.1:8000/projects/<project_id>" \
-H "Authorization: Bearer <your_token>"
```
Replace `<project_id>` with the actual project ID.

### Download Project Data
```bash
curl -X GET "http://127.0.0.1:8000/projects/<project_id>/download" \
-H "Authorization: Bearer <your_token>" \
-o project_<project_id>_data.json
```
Replace `<project_id>` with the actual project ID. The `-o` flag saves the JSON file locally.

## Notes
- All endpoints requiring authentication expect a valid JWT token in the `Authorization` header.
- Replace placeholders like `<your_token>` and `<project_id>` with actual values.
- For more details, see the README.md.

---

## 🗺️ System Architecture

```mermaid
flowchart TD
    User[👤 User] -->|HTTP Requests| FastAPI[🚀 FastAPI App]
    FastAPI -->|Authentication| Auth[🔐 Auth Module]
    FastAPI -->|CRUD Operations| Projects[📁 Projects Module]
    FastAPI -->|AI Generation| CrewAI[🤖 Crew AI Agents]
    FastAPI -->|DB Access| DB[(🗄️ SQLite/PostgreSQL)]
    CrewAI -->|LLM| Ollama[🦙 Ollama Service]
    DB <-->|ORM| SQLAlchemy[🛠️ SQLAlchemy]
```

---

## 🌟 Project Summary & Implementation Report

### ✨ What the Project Does
The Scrumfather is a friendly backend API for managing users and projects. It helps you stay productive with secure authentication, easy project management, and smart AI-powered planning using Crew AI agents and LLMs. 🚀

### 🧩 Implementation Challenges & Solutions

- 🤖 **AI Integration:** Making Crew AI agents and LLMs work together smoothly took some thoughtful design. Solution: Modular agent definitions and a utility function to orchestrate agent workflows.
- 🔐 **Authentication:** Secure JWT-based authentication was set up using FastAPI dependencies for peace of mind.
- 🗄️ **Persistence:** Supporting both SQLite (default) and PostgreSQL (Docker) meant flexible database configuration.
- 🧪 **Testing:** Meaningful tests for authentication and project creation were built using FastAPI's TestClient and pytest.
- 🐳 **Deployment:** Docker Compose makes it easy to spin up AI and database services with just a command.

---

Thanks for checking out The Scrumfather! 😊 If you have questions or want to contribute, feel free to reach out!
