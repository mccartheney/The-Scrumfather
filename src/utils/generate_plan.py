from src.ai.agents import *
from src.ai.tasks import database_task, tasks_task, time_manager_task, user_story_task
from crewai import Crew

User_story_task = user_story_task("Create a new app for managing personal finances")
Database_task = database_task(User_story_task)
Tasks_task = tasks_task(database_task)
Time_manager_task = time_manager_task(tasks_task)

crew = Crew(
    name="Project Planning Crew",
    description="A crew to plan and estimate the development of a new app",
    agents=[product_manager, db_architect, tech_lead, project_manager],
    tasks=[
        User_story_task,
        Database_task,
        Tasks_task,
        Time_manager_task,
    ],
)
