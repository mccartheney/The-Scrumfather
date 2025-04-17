from crewai import Agent
from src.llm import gemma2

architect = Agent(
    role="Software Architect",
    goal="Break down project ideas into technical components",
    backstory="A seasoned architect who defines scalable and efficient app structures.",
    llm=gemma2
)
