import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="AgentHire AI",
    page_icon="🤖",
    layout="wide"
)

# Main Title
st.title(" AgentHire AI")

st.markdown(
    "### AI-Powered Job Recommendation & Career Guidance System"
)

# Sidebar
st.sidebar.header("User Preferences")

experience = st.sidebar.text_input(
    "Experience",
    placeholder="1 year"
)

skills = st.sidebar.text_input(
    "Skills",
    placeholder="Python, FastAPI, MLflow"
)

salary = st.sidebar.text_input(
    "Expected Salary (LPA)",
    placeholder="10"
)

location = st.sidebar.text_input(
    "Preferred Location",
    placeholder="Remote"
)

# Search Button
search_button = st.sidebar.button("Search Jobs")


# Main Logic
if search_button:

    payload = {
        "experience": experience,
        "skills": skills,
        "salary": salary,
        "location": location
    }

    with st.spinner("Searching AI-recommended jobs..."):

        response = requests.post(
            "http://127.0.0.1:8000/jobs",
            json=payload
        )

    if response.status_code == 200:

        data = response.json()

        # AI Advice Section
        st.subheader(" AI Career Advice")

        st.success(data["career_advice"])

        st.divider()

        # Jobs Section
        st.subheader(" Recommended Jobs")

        jobs = data["jobs"]

        if len(jobs) == 0:

            st.warning(
                "No matching jobs found. Try broader skills."
            )

        else:

            for job in jobs:

                with st.container():

                    st.markdown(
                        f"## {job['role']}"
                    )

                    st.write(
                        f" Company: {job['company']}"
                    )

                    st.write(
                        f" Location: {job['location']}"
                    )

                    st.write(
                        f" Match Score: {job['match_percentage']}"
                    )

                    st.write(
                        f" Recommendation: {job['recommendation']}"
                    )

                    st.markdown(
                        f"[Apply Here]({job['apply_link']})"
                    )

                    st.divider()

    else:

        st.error("Backend Error Occurred")

        st.write(response.text)