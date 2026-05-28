from tools.csv_export_tool import export_jobs_to_csv

sample_jobs = [
    {
        "role": "AI Engineer",
        "company": "OpenAI",
        "location": "Remote",
        "match_percentage": "90%",
        "recommendation": "Excellent Match",
        "apply_link": "https://example.com"
    }
]

file = export_jobs_to_csv(sample_jobs)

print(f"CSV Generated: {file}")