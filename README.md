# ✅ Smart Planner CLI – Project Planner with CrewAI

A command-line application built with **Python**, **TextualX**, and **CrewAI** that helps you organize your project idea into a complete technical plan without generating code. This tool is designed to automate the planning phase of your projects, offering a detailed roadmap, architecture suggestions, user stories, technical tasks, and more.

---

## 🧠 1. User Idea Processing

**Goal:** Interpret the textual idea input and generate a technical briefing.

- **Task 1**: Create the `aiapp new` command to start the idea input flow
- **Task 2**: Implement semantic parsing of the project description
- **Task 3**: Generate summary of the idea: goal, stakeholders, scope
- **Task 4**: Detect type of app (API, web, CLI, AI, etc.)
- **Task 5**: Display initial briefing in terminal (via TextualX)

---

## 🏗️ 2. Architecture Suggestion

**Goal:** Suggest the ideal project structure based on the interpreted idea.

- **Task 1**: Map project types to architecture suggestions (rule-based or AI agent-based)
- **Task 2**: Model architecture components (e.g., `agents/`, `api/`, `db/`, etc.)
- **Task 3**: Render a tree view of the suggested structure using TextualX
- **Task 4**: Create `aiapp show-structure` command

---

## 🧾 3. User Stories and Technical Tasks

**Goal:** Generate user stories and technical tasks based on extracted features.

- **Task 1**: Create Agile-style User Story model:
  `As a [persona], I want [action] so that [value]`
- **Task 2**: Implement feature generation based on project scope
- **Task 3**: Break down features into structured technical tasks
- **Task 4**: Create `aiapp generate-stories` command
- **Task 5**: Enable export in JSON, YAML, and Markdown formats

---

## 🤖 4. CrewAI Agent Suggestions

**Goal:** Plan which CrewAI agents are needed and define their interactions.

- **Task 1**: Create a CrewAI agent to recommend other necessary agents
- **Task 2**: Define agent structure: name, function, inputs, outputs, integration
- **Task 3**: Display agent list in a CLI table format
- **Task 4**: Create `aiapp suggest-agents` command

---

## 🧩 5. Technical Planning and Sprint Breakdown

**Goal:** Generate a complete technical roadmap with sprint planning.

- **Task 1**: Analyze dependencies among tasks
- **Task 2**: Group tasks into sprints based on priority and estimated time
- **Task 3**: Estimate complexity and duration per task
- **Task 4**: Create `aiapp plan-sprints` command
- **Task 5**: Render timeline and workload chart

---

## 📚 6. Documentation Planning

**Goal:** Generate a comprehensive documentation plan for the project.

- **Task 1**: Identify topics for technical documentation (architecture, APIs, agents)
- **Task 2**: Suggest structure for README, user guide, and developer docs
- **Task 3**: Create `aiapp doc-plan` command

---

## 📈 7. Progress Validation

**Goal:** Analyze current project progress and suggest next steps.

- **Task 1**: Create `aiapp validate` command to accept user input on current status
- **Task 2**: Compare current progress with original plan
- **Task 3**: List gaps, next actions, and alerts (e.g., missing tests)

---

## 🖥️ 8. TextualX Interface

**Goal:** Present all data in an interactive and visually rich terminal UI.

- **Task 1**: Create a main dashboard with action menu
- **Task 2**: Implement navigable file structure tree
- **Task 3**: Add viewer for user stories and tasks (with filtering and search)
- **Task 4**: Create real-time project progress tracker

---

## 🧪 9. Testing

**Goal:** Ensure CLI stability and modularity.

- **Task 1**: Unit tests for parsing and generation modules
- **Task 2**: Integration tests using complete user idea inputs
- **Task 3**: UI tests with TextualX screens and flows
- **Task 4**: Create `aiapp test` command

---

## 🚀 10. Infrastructure & Deployment

**Goal:** Make the CLI usable on any Python environment.

- **Task 1**: Create `setup.py` or `pyproject.toml` for `pip` install
- **Task 2**: Package as a global CLI: `aiapp` or `crewgen`
- **Task 3**: Write Dockerfile for containerized execution
- **Task 4**: Setup CI pipeline (e.g., GitHub Actions for linting, testing, packaging)

---

# ✅ 11. Project Planning with CrewAI

## 🧠 1. Idea Input + Interpretation

The user provides the app idea in natural language.
The CLI processes the input and outputs:

- Project domain
- Problem to solve
- Final system objective
- Expected stakeholders and users

---

## 🏗️ 2. Technical Architecture Suggestion (No File Generation)

The CLI suggests the most appropriate architecture:

- **FastAPI** with external agents?
- **Pure CLI** with embedded CrewAI agents?
- **Django** for more complex needs?

It also outlines which **folders/components** should be created and why:

- `agents/`: CrewAI-powered intelligent agents
- `api/`: Communication endpoints
- `services/`: Business logic
- `db/`: Database access
- `tests/`: Module-specific tests

---

## 🔧 3. Checklist of Required Components

The CLI provides a checklist for:

- Services to implement
- Suggested REST endpoints
- Expected data models and schemas
- Recommended authentication structure
- Logging, security, error handling practices
- Minimum test coverage per module
- Expected CI/CD scripts and configs

---

## 🧾 4. User Stories and Task Generation

For each key feature, the planner generates:

- ✅ **User Story** (for product team)
- 📌 **Feature Description**
- 🔧 **Technical Tasks**
- 🔗 **Dependencies and prerequisites**

**Example:**

- **User Story**: As an authenticated user, I want to receive personalized content recommendations.
- **Feature**: Recommendation System
- **Tasks**:
  - Create a CrewAI agent that analyzes user history
  - Expose a `GET /recommendations` endpoint
  - Validate backend data inputs
  - Simulate a sample dataset

---

## 📘 5. CrewAI Agent Suggestions

Based on the planned architecture and features, the CLI:

- Lists recommended CrewAI agents
- Defines each agent’s responsibilities and input/output
- Explains how they should interact with the backend and services

---

## 📊 6. Complexity and Time Estimation

For each task/feature, the planner provides:

- 📈 Estimated complexity (low, medium, high)
- ⏱ Estimated development time (in hours)
- 🧑‍💻 Required developer profile (backend, AI, infra)

---

## 📂 7. Sprint Planning

The planner organizes the project into suggested sprints:

- **Sprint 1**: Initial setup + Backend foundation
- **Sprint 2**: CrewAI integration + Testing
- **Sprint 3**: Deployment + Documentation

Includes a suggested timeline and task dependencies.

---

## 🧩 8. Helpful Extra Commands

- `aiapp explain`:
  Explains **why** a certain architecture, agent, or tech stack was suggested.

- `aiapp validate`:
  Takes current progress input and suggests **next steps, warnings, or gaps** in the project.

- `aiapp doc-plan`:
  Generates a **documentation plan** with expected topics for:
  - Technical Docs
  - API Docs
  - End-user Guide
