from crewai import Agent, Task, Crew
import os

os.environ['OPENAI_API_KEY'] = "lick my balls openAi"


# info_agent = Agent (
#   role = "Product manager",
#   goal="create tasks to make a project",
#   backstory = "You make the best tasks in the world",
#   llm=llama2
# )

task = Task(
  description= f"create tasks for the development of the feature ''",
  expected_output="all tasks and the time that each one takes to be finalized, and say if it is backend or front end",
  agent= info_agent
)

crew = Crew (
  agents= [info_agent],
  tasks=[task],
)

result = crew.kickoff()
print (result)
