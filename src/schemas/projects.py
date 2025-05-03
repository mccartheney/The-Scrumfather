# src/models/project.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.connection import Base

# table for projects
class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    idea = Column(String)


    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="projects")
