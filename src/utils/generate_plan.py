from src.ai.agents import *
from src.ai.tasks import database_task, tasks_task, time_manager_task, user_story_task
from crewai import Crew

def generate_crew_for_idea(idea: str):
    user_story = user_story_task(idea)
    db_task = database_task(user_story)
    tasks = tasks_task(db_task)
    time_manager = time_manager_task(tasks)
    return Crew(
        name="Project Planning Crew",
        description="A crew to plan and estimate the development of a new app",
        agents=[product_manager, db_architect, tech_lead, project_manager],
        tasks=[
            user_story,
            db_task,
            tasks,
            time_manager,
        ],
    )
