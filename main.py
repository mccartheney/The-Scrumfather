from fastapi import FastAPI, Depends, HTTPException
from src.routes.auth import get_current_user
from src.database.connection import engine, Base
from src.routes import auth
from src.schemas.user import User
from src.schemas.projects import Project
from src.routes.auth import get_db
from sqlalchemy.orm import Session
from typing import Annotated

from src.utils.generate_plan import crew

# Save the result of crew.kickoff() into a variable
results = crew.kickoff()

# Print all results
for result in results:
    print(result)


# from src.models.projects import Create_project_request

# Base.metadata.create_all(bind=engine)
# app = FastAPI ()
# app.include_router(auth.router)
# db_dependecy = Annotated [Session, Depends(get_db)]




# # hello again jorge, probably you are not here, but i will test every route on main.py first ok, dont be mad
# @app.post("/create_project")
# def create_project(
#     create_project_request: Create_project_request,
#     db: Session = Depends(get_db),
#     user: User = Depends(get_current_user)
# ):
#     # Check if project with the same name already exists for this user
#     for project in user.projects:
#         if project.name == create_project_request.name:
#             raise HTTPException(status_code=409, detail="User already has this project")

#     # Create the new project
#     new_project = Project(name=create_project_request.name,idea=create_project_request.idea, owner=user)
#     db.add(new_project)
#     db.commit()
#     db.refresh(new_project)

#     return {"msg": f"Project '{new_project.name}' created for user '{user.username}'"}
