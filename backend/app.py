from fastapi import FastAPI
from pydantic import BaseModel
from utils.llm_engine import generate_career_advice
from agents.job_search_agent import search_jobs

app = FastAPI()


# Home Route
@app.get("/")
def home():
    return {
        "message": "AgentHire AI Backend Running Successfully"
    }


# Job Request Model
class JobRequest(BaseModel):
    experience: str
    skills: str
    salary: str
    location: str


# Job Search Route
@app.post("/jobs")
def get_jobs(job_request: JobRequest):

    jobs = search_jobs(
        job_request.experience,
        job_request.skills,
        job_request.salary,
        job_request.location
    )

    try:

        career_advice = generate_career_advice(
            job_request.skills,
            job_request.experience
        )

    except Exception as e:

        career_advice = f"LLM Error: {str(e)}"

    return {
        "status": "success",
        "jobs": jobs,
        "career_advice": career_advice
    }