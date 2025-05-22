import logging
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
from datetime import datetime

from src.utils.generate_plan import generate_crew_for_idea
from src.models.projects import Create_project_request

# Initialize FastAPI app
app = FastAPI()

# Include authentication routes
app.include_router(auth.router)

# Create all tables in the database
Base.metadata.create_all(bind=engine)
# Dependency for database session
db_dependency = Annotated[Session, Depends(get_db)]

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'
)
logger = logging.getLogger(__name__)


# Route to create a project for a user
@app.post("/projects/create", status_code=201)
def create_project(
    create_project_request: Create_project_request,
    db: db_dependency,
    user: User = Depends(get_current_user)
):
    logger.info(f"Project creation initiated - User: {user.username}, Project Name: {create_project_request.name}")

    # Check if a project with the same name already exists for the user
    for project in user.projects:
        if project.name == create_project_request.name:
            logger.warning(f"Project creation failed - Duplicate project name '{create_project_request.name}' for user {user.username}")
            raise HTTPException(status_code=409, detail="User already has this project")

    # Run AI generation logic
    try:
        logger.info(f"Starting AI generation for project: {create_project_request.name}")
        crew_instance = generate_crew_for_idea(create_project_request.idea)
        ai_results = crew_instance.kickoff()
        if not ai_results:
            logger.error(f"AI generation failed - No results returned for project: {create_project_request.name}")
            raise ValueError("AI generation returned no results")

        # Convert TaskOutput objects to JSON-serializable format
        ai_results_serializable = [
            result.to_dict() if hasattr(result, "to_dict") else str(result)
            for result in ai_results
        ]
        ai_results_json = json.dumps(ai_results_serializable)
        logger.info(f"AI generation completed successfully for project: {create_project_request.name}")
    except Exception as e:
        logger.error(f"AI generation failed for project {create_project_request.name}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"AI generation failed: {str(e)}")

    try:
        # Create the new project with AI-generated data
        new_project = Project(
            name=create_project_request.name,
            idea=create_project_request.idea,
            owner=user,
            ai_data=ai_results_json
        )
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        logger.info(f"Project created successfully - ID: {new_project.id}, Name: {new_project.name}, User: {user.username}")
    except Exception as e:
        logger.error(f"Database error while creating project {create_project_request.name}: {str(e)}", exc_info=True)
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create project in database")

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
    logger.info(f"Fetching all projects for user: {user.username}")
    try:
        projects = [{"id": project.id, "name": project.name, "idea": project.idea} for project in user.projects]
        logger.info(f"Successfully retrieved {len(projects)} projects for user {user.username}")
        return {"projects": projects}
    except Exception as e:
        logger.error(f"Error fetching projects for user {user.username}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to fetch projects")

# Route to get details of a specific project
@app.get("/projects/{project_id}", status_code=200)
def get_project_details(
    project_id: int,
    db: db_dependency,
    user: User = Depends(get_current_user)
):
    logger.info(f"Fetching details for project ID: {project_id}, User: {user.username}")
    try:
        project = db.query(Project).filter(Project.id == project_id, Project.owner_id == user.id).first()
        if not project:
            logger.warning(f"Project not found - ID: {project_id}, User: {user.username}")
            raise HTTPException(status_code=404, detail="Project not found")

        logger.info(f"Successfully retrieved project details - ID: {project_id}, Name: {project.name}")
        return {
            "id": project.id,
            "name": project.name,
            "idea": project.idea,
            "ai_data": json.loads(project.ai_data)
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching project details - ID: {project_id}, User: {user.username}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to fetch project details")

@app.get("/projects/{project_id}/download", status_code=200)
def download_project_data(
    project_id: int,
    db: db_dependency,
    user: User = Depends(get_current_user)
):
    logger.info(f"Download request for project ID: {project_id}, User: {user.username}")
    try:
        project = db.query(Project).filter(Project.id == project_id, Project.owner_id == user.id).first()
        if not project:
            logger.warning(f"Project not found for download - ID: {project_id}, User: {user.username}")
            raise HTTPException(status_code=404, detail="Project not found")

        # Create a JSON file with project data
        file_path = f"project_{project_id}_data.json"
        try:
            with open(file_path, "w") as file:
                json.dump({
                    "id": project.id,
                    "name": project.name,
                    "idea": project.idea,
                    "ai_data": json.loads(project.ai_data)
                }, file)
            logger.info(f"Project data file created successfully - Path: {file_path}")
        except Exception as e:
            logger.error(f"Error creating project data file - ID: {project_id}: {str(e)}", exc_info=True)
            raise HTTPException(status_code=500, detail="Failed to create project data file")

        # Return the file as a response
        logger.info(f"Project data download completed - ID: {project_id}, User: {user.username}")
        return FileResponse(file_path, media_type="application/json", filename=file_path)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during project download - ID: {project_id}, User: {user.username}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to download project data")
