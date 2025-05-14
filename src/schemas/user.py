# src/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.connection import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    projects = relationship("Project", back_populates="owner", cascade="all, delete-orphan")
