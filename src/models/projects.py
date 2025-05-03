from pydantic import BaseModel

# request model for project request
class Create_project_request (BaseModel) :
  name : str
  idea : str
