from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    #
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_career_advice(
    skills,
    experience,
    missing_skills
):

    prompt = f"""
    User Skills:
    {skills}

    Experience:
    {experience}

    Missing Skills:
    {missing_skills}

    Give:
    1. Best AI/ML career roles
    2. Important missing skills
    3. Roadmap to reach high-paying AI jobs
    4. Interview preparation advice
    5. Which technologies are trending in industry

    Keep response practical, short, and professional.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
# def generate_career_advice(skills, experience):

#     prompt = f"""
#     User Skills: {skills}
#     Experience: {experience}

#     Give:
#     1. Best AI/ML roles suitable
#     2. Missing skills
#     3. Career improvement advice
#     4. Interview preparation suggestions

#     Keep response short and professional.
#     """

#     response = client.chat.completions.create(
#         # model="llama3-8b-8192",
#         model="llama-3.1-8b-instant",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response.choices[0].message.content