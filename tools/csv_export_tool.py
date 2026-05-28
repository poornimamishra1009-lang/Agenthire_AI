import csv


def export_jobs_to_csv(jobs):

    filename = "recommended_jobs.csv"

    with open(
        filename,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([
            "Role",
            "Company",
            "Location",
            "Match Percentage",
            "Recommendation",
            "Apply Link"
        ])

        # Job Rows
        for job in jobs:

            writer.writerow([
                job.get("role", ""),
                job.get("company", ""),
                job.get("location", ""),
                job.get("match_percentage", ""),
                job.get("recommendation", ""),
                job.get("apply_link", "")
            ])

    return filename