from agents.resume_agent import extract_resume_skills

from agents.skill_gap_agent import analyze_skill_gap

from utils.llm_engine import generate_career_advice


# Step 1: Extract Resume Skills
resume_data = extract_resume_skills(
    "sample_resume.txt"
)

detected_skills = resume_data[
    "detected_skills"
]

skills_string = ", ".join(
    detected_skills
)

print("\n[Resume Agent]")
print("Detected Skills:")
print(detected_skills)


# Step 2: Skill Gap Analysis
skill_gap = analyze_skill_gap(
    skills_string
)

print("\n[Skill Gap Agent]")
print("Missing Skills:")
print(skill_gap["missing_skills"])


# Step 3: LLM Career Advice
career_advice = generate_career_advice(
    skills_string,
    "1 year",
    skill_gap["missing_skills"]
)

print("\n[Career Advice Agent]")
print(career_advice)