from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import FileResponse
from src.routes.auth import get_current_user
from src.database.connection import engine, Base
from src.routes import auth
from src.schemas.user import User
from src.schemas.projects import Project
from src.routes.auth import get_db
from sqlalchemy.orm import Session
from typing import Annotated
import json

from src.utils.generate_plan import crew
from src.models.projects import Create_project_request

# Initialize FastAPI app
app = FastAPI()

# Include authentication routes
app.include_router(auth.router)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Dependency for database session
db_dependency = Annotated[Session, Depends(get_db)]

# Route to create a project for a user
@app.post("/projects/create", status_code=201)
def create_project(
    create_project_request: Create_project_request,
    db: db_dependency,
    user: User = Depends(get_current_user)
):
    # Check if a project with the same name already exists for the user
    for project in user.projects:
        if project.name == create_project_request.name:
            raise HTTPException(status_code=409, detail="User already has this project")

    # Run AI generation logic
    try:
        ai_results = crew.kickoff()
        if not ai_results:
            raise ValueError("AI generation returned no results")

        # Convert TaskOutput objects to JSON-serializable format
        ai_results_serializable = [
            result.to_dict() if hasattr(result, "to_dict") else str(result)
            for result in ai_results
        ]
        ai_results_json = json.dumps(ai_results_serializable)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI generation failed: {str(e)}")

    # Create the new project with AI-generated data
    new_project = Project(
        name=create_project_request.name,
        idea=create_project_request.idea,
        owner=user,
        ai_data=ai_results_json  # Store AI results in the project
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "msg": f"Project '{new_project.name}' created for user '{user.username}'",
        "ai_results": ai_results_serializable
    }

# Route to get all projects of the current user
@app.get("/projects", status_code=200)
def get_user_projects(
    db: db_dependency,
    user: User = Depends(get_current_user)
):
    return {"projects": [{"id": project.id, "name": project.name, "idea": project.idea} for project in user.projects]}

# Route to get details of a specific project
@app.get("/projects/{project_id}", status_code=200)
def get_project_details(
    project_id: int,
    db: db_dependency,
    user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id, Project.owner_id == user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "id": project.id,
        "name": project.name,
        "idea": project.idea,
        "ai_data": json.loads(project.ai_data)  # Parse and return AI data
    }
@app.get("/projects/{project_id}/download", status_code=200)
def download_project_data(
    project_id: int,
    db: db_dependency,
    user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id, Project.owner_id == user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Create a JSON file with project data
    file_path = f"project_{project_id}_data.json"
    with open(file_path, "w") as file:
        json.dump({"id": project.id, "name": project.name, "idea": project.idea, "ai_data": json.loads(project.ai_data)}, file)

    # Return the file as a response
    return FileResponse(file_path, media_type="application/json", filename=file_path)
