from crewai import Task
from src.agents.product_manager_agent import product_manager

def user_stories_task (task_which_that_depends) :
  return Task(
      description="""Based on the system architecture and tech stack defined in the previous task,
      write comprehensive Agile-style user stories with focus on functionality and user experience.
      Consider the roles and technologies mentioned in the architecture when creating stories.""",
      expected_output = (
        "Comprehensive user stories written in Agile format (As a [user], I want [feature], so that [benefit]). "
        "Include both core and optional features for the MVP phase of the application. "
        "Focus on stories that highlight key functionality and user value. "
        "Include engagement elements such as personalization, notifications, and progress tracking. "
        "Ensure stories cover all essential user workflows and interactions. "
        "Reference the architecture and tech stack from the previous task when relevant."
      ),
      agent=product_manager,
      depends_on=[task_which_that_depends],
      output_file="/output/user_stories.md"
  )
