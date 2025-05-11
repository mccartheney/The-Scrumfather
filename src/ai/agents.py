from crewai import Agent
from src.ai.llm import gemma2 as llm

product_manager = Agent(
    role="Product Manager",
    goal="Generate comprehensive user stories for the given app idea",
    backstory="You are a detail-oriented product manager experienced in app development",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

db_architect = Agent(
    role="Database Architect",
    goal="Design the database structure for the app based on user stories",
    backstory="Expert in designing scalable database schemas for modern web apps",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

tech_lead = Agent(
    role="Tech Lead",
    goal="Break the app into detailed development tasks based on the database and features",
    backstory="Seasoned full-stack developer and software architect",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

project_manager = Agent(
    role="Project Manager",
    goal="Estimate time to complete each task, considering the average dev team speed",
    backstory="Skilled in Agile planning and time estimation",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
