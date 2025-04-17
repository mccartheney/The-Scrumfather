from crewai import Task
from src.agents.db_designer_agent import db_designer

def db_structure_task(task_which_that_depends):
    return Task(
        description="Design a normalized SQL database schema to support the features described in the user stories.",
        expected_output=(
            "A complete database schema optimized for performance and scalability. "
            "Include efficient data structures for all application features described in the user stories. "
            "Design tables with proper normalization and indexing strategies. "
            "Include analytics tables for tracking user behavior and application metrics. "
            "List each table, its fields, data types, relationships, and indexes. "
            "Explain how the schema supports the application features and performance requirements. "
            "Reference specific user stories and architecture components when explaining design decisions."
        ),
        agent=db_designer,
        depends_on=[task_which_that_depends],
        output_file="/output/db_structure.md"
    )
