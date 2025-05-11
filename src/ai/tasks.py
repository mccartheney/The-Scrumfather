from src.ai.agents import *
from crewai import Task

def user_story_task(app_idea: str):
    return Task(
        description=f"Generate user stories for: {app_idea}",
        expected_output="List of user stories with priorities",
        agent=product_manager,
        depends_on=None,
        # output_file="user_stories",
    )

def database_task(depends_on):
    return Task(
        description="Design database structure based on user stories",
        expected_output="Normalized database schema with tables and fields",
        agent=db_architect,
        depends_on=depends_on,
        # output_file="database_schema",
    )

def tasks_task(depends_on):
    return Task(
        description="Break the project into technical development tasks",
        expected_output="List of development tasks grouped by feature/module",
        agent=tech_lead,
        depends_on=depends_on,
        # output_file="development_tasks",
    )

def time_manager_task(depends_on):
    return Task(
        description="Estimate time required for each development task",
        expected_output="Timeline with hours/days per task",
        agent=project_manager,
        depends_on=depends_on,
        # output_file="time_estimation",
    )
