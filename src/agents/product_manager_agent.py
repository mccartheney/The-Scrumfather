from crewai import Agent
from src.llm import gemma2

product_manager = Agent(
    role="Product Manager",
    goal="Translate features into clear, prioritized user stories",
    backstory="An expert in agile methodology and lean product development.",
    llm=gemma2
)
