from crewai import Crew

# import tasks
from src.tasks.assign_user_stories_task import assing_user_stories_task
from src.tasks.create_db_structure_task import db_structure_task
from src.tasks.create_user_stories_task import user_stories_task
from src.tasks.devops_task import devops_task
from src.tasks.initial_task import initial_task

# import agents
from src.agents.architect_agent import architect
from src.agents.db_designer_agent import db_designer
from src.agents.devops_adviser_agent import devops_advisor
from src.agents.product_manager_agent import product_manager
from src.agents.task_planner_agent import task_planner

# Define the project idea
idea = 'a clone of pinterest that have focus in hair colors'

# Define team roles
roles = ["Frontend Developer", "Backend Developer", "devops"]

# Define tasks structure
task_to_create_system_architecture = initial_task(idea=idea, roles=roles)
task_to_create_user_stories = user_stories_task(task_which_that_depends=task_to_create_system_architecture)
task_to_create_db_structure = db_structure_task(task_which_that_depends=task_to_create_user_stories)
task_to_assign_user_stories = assing_user_stories_task(task_which_that_depends=task_to_create_db_structure)
task_to_plan_infra = devops_task(task_which_that_depends=task_to_assign_user_stories)

# Create the crew with all agents and tasks
crew = Crew(
  agents=[
    architect,
    product_manager,
    db_designer,
    task_planner,
    devops_advisor,
  ],
  tasks=[
    task_to_create_system_architecture,
    task_to_create_user_stories,
    task_to_create_db_structure,
    task_to_assign_user_stories,
    task_to_plan_infra,
  ],
  verbose=True
)
