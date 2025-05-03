from fastapi import FastAPI, Depends
from src.routes.auth import get_current_user
from src.database.connection import engine, Base
from src.routes import auth
from src.schemas.user import User
from src.schemas.projects import Project

Base.metadata.create_all(bind=engine)
app = FastAPI ()
app.include_router(auth.router)

@app.get("/")
def user (user: User = Depends(get_current_user)) :
    return {"msg": f" {user.username}, authenticated uhuhuhuhu"}
