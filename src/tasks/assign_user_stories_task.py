from crewai import Task
from src.agents.task_planner_agent import task_planner

def assing_user_stories_task (task_which_that_depends) :
 return Task(
      description="""Based on the user stories, system architecture, and database schema from previous tasks,
      break down the implementation into detailed technical tasks with focus on quality and maintainability.
      Assign tasks to frontend, backend, and devops roles, considering the tech stack and database design.""",
      expected_output = (
        "A comprehensive breakdown of technical tasks needed to implement the application features. "
        "Group tasks by role: Frontend Developer, Backend Developer, and DevOps Engineer. "
        "For each task, provide: "
        "1. A clear description of the implementation goal "
        "2. Complexity estimate (low/medium/high) with justification "
        "3. Technical considerations and potential challenges "
        "4. Dependencies on other tasks "
        "5. Estimated effort in story points "
        "Include tasks for core functionality, user experience features, and system integration. "
        "Reference specific user stories, architecture components, and database tables when relevant."
      ),
      agent=task_planner,
      depends_on=[task_which_that_depends],
      output_file="/output/assign_tasks.md"
  )
