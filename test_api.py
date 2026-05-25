from utils.job_api import fetch_jobs

jobs = fetch_jobs()

print(jobs[0])