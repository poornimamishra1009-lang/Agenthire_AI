def analyze_skill_gap(user_skills):

    trending_skills = [
        "Python",
        "FastAPI",
        "Docker",
        "MLflow",
        "LLMs",
        "RAG",
        "Vector Databases",
        "Kubernetes",
        "AWS",
        "Prompt Engineering"
    ]

    user_skill_list = [
        skill.strip().lower()
        for skill in user_skills.split(",")
    ]

    missing_skills = []

    for skill in trending_skills:

        if skill.lower() not in user_skill_list:

            missing_skills.append(skill)

    return {
        "current_skills": user_skill_list,
        "missing_skills": missing_skills
    }