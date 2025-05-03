from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.schemas.user import User
from src.database.connection import SessionLocal, engine, Base
import src.utils.auth as auth
from typing import Annotated
from src.models.user import User_register_model, User_login_model
from src.utils import auth

# create all table if they dont exists
Base.metadata.create_all(bind=engine)

# init route api and auth scheme
router = APIRouter(
    prefix="/auth",
    tags = ["auth"]
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# function to get db and pass to the route
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependecy = Annotated [Session, Depends(get_db)]

@router.post("/register", status_code=201)
def register(db : db_dependecy, user_register_model : User_register_model ):
    # get user in db by username gived by user
    user = db.query(User).filter(User.username == user_register_model.username).first()
    # if user exists throw a error
    if user:
        raise HTTPException(status_code=409, detail="User already exists")

    # hash the passwoed aand create user
    hashed = auth.hash_password(user_register_model.password)
    new_user = User(
        username=user_register_model.username,
        hashed_password=hashed,
        projects = []
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # if sucess warn user
    return {"msg": "New User Created"}

@router.post("/login")
def login(db : db_dependecy, user_login_model : User_login_model):
    # get user in database by username gived by user
    user = db.query(User).filter(User.username == user_login_model.username).first()
    # if wrong credentials throw a error
    if not user or not auth.verify_password(user_login_model.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # create the token for user and return to user
    token = auth.create_token({"sub": user.username})
    assert token
    return {"access_token": token, "token_type": "bearer"}

# function to get user
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    # get username from token
    username = auth.verify_token(token)

    # if invalid token
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token")

    # if dont have user throw a error, otherwise return the user
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
