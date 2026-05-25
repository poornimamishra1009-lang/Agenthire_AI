from utils.llm_engine import generate_career_advice

response = generate_career_advice(
    "Python, FastAPI, MLflow",
    "1 year"
)

print(response)