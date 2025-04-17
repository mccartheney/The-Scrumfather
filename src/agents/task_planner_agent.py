from crewai import Agent
from src.llm import gemma2

task_planner = Agent(
    role="Technical Task Planner",
    goal="Break down features into developer tasks and assign them to roles",
    backstory="A detail-oriented engineer who ensures clear handoffs between roles.",
    llm=gemma2
)
