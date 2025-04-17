from crewai import Task
from src.agents.architect_agent import architect

def initial_task (idea, roles) :
  return Task(
      description=f"Given the idea: '{idea}', define a robust, scalable system architecture with focus on performance and maintainability, suggest tech stack for: {roles}",
      expected_output = (
        "A modular, scalable, and maintainable system architecture for the application. "
        "Include a breakdown of key microservices components, their responsibilities, and communication patterns. "
        "Focus on performance optimization and system reliability. "
        "Recommend a suitable tech stack for frontend, backend, database, and infrastructure with emphasis on proven technologies. "
        "Include considerations for scalability, monitoring, and fault tolerance. "
        "Provide clear context for subsequent tasks by explaining how each component relates to the overall application goals."
      ),
      agent=architect,
      output_file="/output/arquitect.md"
  )
