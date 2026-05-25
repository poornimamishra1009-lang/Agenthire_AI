from utils.job_api import fetch_jobs


def search_jobs(experience, skills, salary, location):

    jobs = fetch_jobs()

    user_salary = int(salary.replace("LPA", "").strip())

    user_skills = [skill.strip().lower() for skill in skills.split(",")]

    filtered_jobs = []

    for job in jobs:
        ai_keywords = [
            "ai",
            "ml",
            "machine learning",
            "python",
            "llm",
            "genai",
            "data",
            "backend",
            "developer",
            "engineer",
            "software"
        ]
        role = job["role"].lower()
        # role = job["role"].lower()

        tags = [tag.lower() for tag in job.get("tags", [])]

        combined_text = role + " " + " ".join(tags)
        combined_words = combined_text.split()
        job_is_relevant = True
        # relevant_roles = [
        #     "engineer",
        #     "developer",
        #     "machine learning",
        #     "ai",
        #     "ml",
        #     "data scientist",
        #     "python",
        #     "backend",
        #     "software"
        # ]

        # job_is_relevant = False

        # for keyword in relevant_roles:

        #     if keyword in role:
        #         job_is_relevant = True
        #         break
        # matched_skills = []
        matched_skills = set()
        for skill in user_skills:

            # if skill in role:
            # if skill in combined_words:
            for word in combined_words:

                if skill in word:

                    # matched_skills.append(skill)
                    matched_skills.add(skill)
                    break
                matched_skills.add(skill)
                # matched_skills.append(skill)

        # Salary conversion
        salary_max = job.get("salary_max", 0)

        # Convert remote salaries to approximate LPA
        estimated_lpa = int(salary_max / 100000) if salary_max else 0
        if (
            job_is_relevant
            and len(matched_skills) > 0
            and (
                estimated_lpa >= user_salary
                or estimated_lpa == 0
            )
        ):
        # if (
        #     len(matched_skills) > 0
        #     and estimated_lpa >= user_salary
        # ):
            match_percentage = min(
                int(
                    (len(matched_skills) / len(user_skills)) * 100
                ),
                100
            )
            # match_percentage = int(
            #     (len(matched_skills) / len(user_skills)) * 100
            # )
            if match_percentage >= 80:
                recommendation = "Excellent Match"

            elif match_percentage >= 50:
                recommendation = "Good Match"

            else:
                recommendation = "Average Match"
            filtered_jobs.append({
                "role": job["role"],
                "company": job["company"],
                "location": job["location"],
                "salary_estimate_lpa": estimated_lpa,
                "matched_skills": matched_skills,
                "match_percentage": f"{match_percentage}%",
                "recommendation": recommendation,
                "apply_link": job["apply_link"]
            })

    return filtered_jobs