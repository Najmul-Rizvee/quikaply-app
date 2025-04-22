import streamlit as st
from modules.job_scraper import get_jobs
from modules.resume_customizer import customize_resume
from modules.tracker import save_application
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="QuikAply — AI Job Assistant", layout="wide")
st.title("💼 QuikAply — Apply Smarter. Faster.")

mode = st.radio("Mode", ["Mock Jobs", "Live Jobs (Indeed.ca)"], horizontal=True)
job_title = st.text_input("Job Title", "Technical Support")
location = st.text_input("Location", "Vancouver, BC")

if st.button("Search Jobs"):
    with st.spinner("Fetching jobs..."):
        jobs = get_jobs(job_title, location, mock=(mode == "Mock Jobs"))
        st.session_state["jobs"] = jobs

if "jobs" in st.session_state:
    for idx, job in enumerate(st.session_state["jobs"]):
        with st.expander(f"{job['title']} at {job['company']}"):
            st.write(f"📍 {job['location']}")
            st.write(job["description"])
            if st.button(f"Customize Resume #{idx+1}"):
                customized = customize_resume(job["description"], API_KEY)
                st.download_button("⬇️ Download Resume", customized, file_name="custom_resume.docx")
                save_application(job)
