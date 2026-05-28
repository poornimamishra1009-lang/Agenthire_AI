# from mcp.context_manager import ContextManager


# class AgentCoordinator:

#     def __init__(self):

#         self.context = ContextManager()

#     def update(self, key, value):

#         self.context.update_context(key, value)

#     def get_full_context(self):

#         return self.context.get_context()

from mcp.context_manager import ContextManager

from agents.skill_gap_agent import analyze_skill_gap

from agents.job_search_agent import search_jobs

from utils.llm_engine import generate_career_advice
from tools.csv_export_tool import export_jobs_to_csv

class AgentCoordinator:

    def __init__(self):

        self.context = ContextManager()

    def run_agents(
        self,
        experience,
        skills,
        salary,
        location
    ):

        # Store Context
        self.context.update_context(
            "experience",
            experience
        )

        self.context.update_context(
            "skills",
            skills
        )

        self.context.update_context(
            "salary",
            salary
        )

        self.context.update_context(
            "location",
            location
        )

        # Run Job Agent
        jobs = search_jobs(
            experience,
            skills,
            salary,
            location
        )
        # MCP Tool Execution
        csv_file = export_jobs_to_csv(
            jobs
        )
        # Run Skill Gap Agent
        skill_gap = analyze_skill_gap(
            skills
        )

        # Run Career Advice Agent
        career_advice = generate_career_advice(
            skills,
            experience,
            skill_gap["missing_skills"]
        )
        # career_advice = generate_career_advice(
        #     skills,
        #     experience
        # )
        return {
            "context": self.context.get_context(),
            "jobs": jobs,
            "skill_gap": skill_gap,
            "career_advice": career_advice,
            "csv_file": csv_file
        }
        # return {
        #     "context": self.context.get_context(),
        #     "jobs": jobs,
        #     "skill_gap": skill_gap,
        #     "career_advice": career_advice
        # }