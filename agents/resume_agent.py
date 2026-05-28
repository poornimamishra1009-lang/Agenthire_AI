from tools.resume_reader_tool import read_resume


def extract_resume_skills(file_path):

    resume_text = read_resume(file_path)

    known_skills = [
        "python",
        "fastapi",
        "mlflow",
        "docker",
        "git",
        "llms",
        "rag",
        "aws",
        "kubernetes",
        "sql",
        "machine learning",
        "deep learning",
        "computer vision",
        "nlp"
    ]

    detected_skills = []

    resume_lower = resume_text.lower()

    for skill in known_skills:

        if skill in resume_lower:

            detected_skills.append(skill)

    return {
        "resume_text": resume_text,
        "detected_skills": detected_skills
    }