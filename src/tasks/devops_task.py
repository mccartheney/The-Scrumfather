from crewai import Task
from src.agents.devops_adviser_agent import devops_advisor

def devops_task(task_which_that_depends):
    return Task(
        description="Plan CI/CD and infrastructure for the project (local dev, staging, prod).",
        expected_output=(
            "A comprehensive DevOps plan with emphasis on system reliability: "
            "1. Infrastructure setup for local dev, staging, and production environments using reliable cloud providers "
            "2. CI/CD pipeline design with automated testing and deployment strategies "
            "3. Monitoring and observability tools for tracking application performance and resource usage "
            "4. Security measures to protect user data and ensure compliance "
            "5. Recommendations for containerization and orchestration to optimize resource utilization "
            "6. Strategies for high availability, disaster recovery, and performance optimization "
            "Include specific tools and technologies that support robust application deployment and operation. "
            "Reference the architecture, database design, and technical tasks when explaining infrastructure decisions."
        ),
        agent=devops_advisor,
        depends_on=[task_which_that_depends],
        output_file="/output/devops.md"
    )
