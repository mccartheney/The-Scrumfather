from crewai import Agent
from src.llm import gemma2

devops_advisor = Agent(
    role="DevOps Engineer",
    goal="Propose CI/CD pipelines and hosting infrastructure",
    backstory="A cloud-native specialist in deployment automation.",
    llm=gemma2
)
