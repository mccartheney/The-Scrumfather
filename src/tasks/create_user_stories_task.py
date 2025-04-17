from crewai import Task
from src.agents.product_manager_agent import product_manager

def user_stories_task(task_which_that_depends):
    return Task(
        description="From the idea, write 6-10 Agile-style user stories.",
        expected_output=(
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
