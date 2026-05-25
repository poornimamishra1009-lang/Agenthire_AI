import requests


def fetch_jobs():

    url = "https://remoteok.com/api"

    response = requests.get(url)

    data = response.json()

    cleaned_jobs = []

    # Skip first item (metadata)
    for job in data[1:]:

        cleaned_job = {
            "role": job.get("position", "Not Available"),
            "company": job.get("company", "Not Available"),
            "location": job.get("location", "Remote"),
            "salary_min": job.get("salary_min", 0),
            "salary_max": job.get("salary_max", 0),
            "tags": job.get("tags", []),
            "apply_link": job.get("apply_url", "No Link")
        }
        cleaned_jobs.append(cleaned_job)

    return cleaned_jobs