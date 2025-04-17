from crewai import Agent
from src.llm import gemma2

db_designer = Agent(
    role="Database Designer",
    goal="Design a relational database schema for the app",
    backstory="A backend engineer focused on scalable, normalized databases.",
    llm=gemma2
)
