import streamlit as st
st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖",
    layout="wide"
)
from pypdf import PdfReader
import pandas as pd
from ats import extract_skills, calculate_ats
from skills import ROLE_SKILLS

from career import (
    generate_resume_feedback,
    skill_gap_analysis,
    learning_roadmap,
    get_interview_questions,
    recommended_projects
)

from report import generate_report
from charts import show_skill_chart

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.main {
    background-color:#f6f8fc;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 15px;
    padding: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

div[data-testid="stMetric"] label {
    color: #222222 !important;
}

div[data-testid="stMetricValue"] {
    color: #111111 !important;
    font-weight: bold !important;
}

div[data-testid="stMetricDelta"] {
    color: #16a34a !important;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-weight:bold;
    font-size:17px;
}

.skill{
    background:#E8F0FE;
    padding:8px;
    border-radius:8px;
    margin:5px;
    display:inline-block;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HISTORY FILE
# ==========================

try:
    open("history.txt","a").close()
except:
    pass

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🤖 AI Career Copilot")

menu = st.sidebar.radio(
    "Navigation",
    [
        "📄 Resume Analyzer",
        "📜 Recent Analyses",
        "📊 ATS Statistics",
        "ℹ️ About"
    ]
)

# ===================================================
# RESUME ANALYZER
# ===================================================

if menu=="📄 Resume Analyzer":

    st.markdown("# 🤖 AI Career Copilot")

    st.markdown(
        "### AI Powered Resume Analysis & Career Guidance"
    )

    st.info(
        "Upload your resume and compare it with a Job Description."
    )

    c1,c2,c3=st.columns(3)

    with c1:
        st.metric(
            "📄 Resume Database",
            "100+",
            "Growing"
        )

    with c2:
        st.metric(
            "🛠 Supported Skills",
            "100+",
            "Updated"
        )

    with c3:
        st.metric(
            "🎯 ATS Accuracy",
            "95%",
            "Excellent"
        )

    st.divider()

    uploaded_file=st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    job_description=st.text_area(
        "Paste Job Description",
        height=220
    )

    job_role=st.selectbox(
        "Target Role",
        list(ROLE_SKILLS.keys())
    )

    if uploaded_file:

        pdf=PdfReader(uploaded_file)

        resume_text=""

        for page in pdf.pages:

            txt=page.extract_text()

            if txt:

                resume_text+=txt

        resume_skills=extract_skills(resume_text)

        st.success("Resume uploaded successfully!")

        st.markdown("## 🛠 Skills Detected")

        cols=st.columns(3)

        for i,skill in enumerate(resume_skills):

            cols[i%3].success(skill)
                    # ==========================================
        # ATS ANALYSIS
        # ==========================================

        if job_description.strip():

            job_skills = extract_skills(job_description)

            ats_score = round(
                calculate_ats(
                    resume_skills,
                    job_skills
                ),
                2
            )

            missing_skills = list(
                set(job_skills) -
                set(resume_skills)
            )

            st.divider()

            st.markdown("## 📊 ATS Dashboard")

            m1, m2, m3 = st.columns(3)

            if ats_score >= 80:
                score_status = "🟢 Excellent"
            elif ats_score >= 60:
                score_status = "🟡 Good"
            else:
                score_status = "🔴 Needs Improvement"

            with m1:
                st.metric(
                    "ATS Score",
                    f"{ats_score}%",
                    score_status
                )
                st.progress(ats_score / 100)

            with m2:
                st.metric(
                    "Skills Found",
                    len(resume_skills)
                )

            with m3:
                st.metric(
                    "Missing Skills",
                    len(missing_skills)
                )

            st.divider()

            st.markdown("## ❌ Missing Skills")

            if missing_skills:

                cols = st.columns(3)

                for i, skill in enumerate(missing_skills):
                    cols[i % 3].warning(skill)

            else:
                st.success(
                    "🎉 No missing skills detected!"
                )

            # Skill Chart
            show_skill_chart(
                resume_skills,
                missing_skills
            )

            # ==========================================
            # AI RESUME FEEDBACK
            # ==========================================

            st.divider()

            st.markdown("## 🤖 AI Resume Feedback")

            feedback = generate_resume_feedback(
                ats_score,
                missing_skills
            )

            for tip in feedback:
                st.info(tip)

            # ==========================================
            # SKILL GAP ANALYSIS
            # ==========================================

            st.divider()

            st.markdown("## 🚀 Skill Gap Analysis")

            gaps = skill_gap_analysis(
                job_role,
                resume_skills
            )

            if gaps:

                cols = st.columns(3)

                for i, gap in enumerate(gaps):
                    cols[i % 3].error(gap)

            else:

                st.success(
                    "✅ You already match this role very well!"
                )

            # ==========================================
            # LEARNING ROADMAP
            # ==========================================

            st.divider()

            st.markdown("## 📚 Learning Roadmap")

            roadmap = learning_roadmap(gaps)

            if roadmap:

                for step in roadmap:
                    st.write("✅", step)

            else:

                st.success(
                    "No learning roadmap required."
                )
                            # ==========================================
            # INTERVIEW QUESTIONS
            # ==========================================

            st.divider()

            st.markdown("## 🎤 Interview Questions")

            questions = get_interview_questions(job_role)

            if questions:

                for i, question in enumerate(questions, start=1):

                    with st.expander(f"Question {i}"):

                        st.write(question)

            else:

                st.info("No interview questions available.")

            # ==========================================
            # PROJECT RECOMMENDATIONS
            # ==========================================

            st.divider()

            st.markdown("## 💼 Recommended Projects")

            projects = recommended_projects(job_role)

            cols = st.columns(2)

            for i, project in enumerate(projects):

                cols[i % 2].success(project)

            # ==========================================
            # DOWNLOAD REPORT
            # ==========================================

            st.divider()

            st.markdown("## 📄 Career Report")

            report = generate_report(

                ats_score,

                resume_skills,

                missing_skills,

                job_role,

                gaps,

                roadmap,

                projects,

                questions

            )

            with open("history.txt", "a") as file:

                file.write(
                    f"ATS: {ats_score}% | Role: {job_role}\n"
                )

            st.download_button(

                "📥 Download Career Report",

                report,

                file_name="AI_Career_Report.txt",

                mime="text/plain"

            )

# ===================================================
# RECENT ANALYSES
# ===================================================

elif menu == "📜 Recent Analyses":

    st.title("📜 Recent Analyses")

    try:

        with open("history.txt", "r") as file:

            history = file.readlines()

        if history:

            st.success(f"Total Analyses: {len(history)}")

            for item in reversed(history):

                st.write("•", item.strip())

        else:

            st.info("No previous analyses found.")

    except FileNotFoundError:

        st.info("History file not found.")

# ===================================================
# ATS STATISTICS
# ===================================================

elif menu == "📊 ATS Statistics":

    st.title("📊 ATS Statistics")

    total_roles = len(ROLE_SKILLS)
    total_skills = sum(len(v) for v in ROLE_SKILLS.values())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Supported Roles", total_roles)

    with col2:
        st.metric("Total Skills", total_skills)

    st.divider()

    st.subheader("🎯 Supported Career Paths")

    for role in ROLE_SKILLS.keys():
        st.write(f"✅ {role}")

    st.divider()

    st.subheader("📈 AI Career Copilot Summary")

    st.success(f"""
✅ Supported Roles: {total_roles}

✅ Total Skills in Database: {total_skills}

✅ Resume PDF Parsing

✅ ATS Score Calculation

✅ Skill Extraction

✅ Skill Gap Analysis

✅ Career Guidance

✅ Interview Questions

✅ Learning Roadmap
""")
    
# ===================================================
# ABOUT
# ===================================================

elif menu == "ℹ️ About":

    st.title("🤖 AI Career Copilot")

    st.markdown("""
### 🚀 Features

- Resume PDF Parsing
- ATS Score
- Skill Extraction
- Missing Skill Detection
- AI Resume Feedback
- Skill Gap Analysis
- Learning Roadmap
- Interview Questions
- Project Recommendations
- Career Report Download

---

### 🛠 Built With

- Python
- Streamlit
- Pandas
- PyPDF
- NLP

---

### 👩‍💻 Developer

**Shruti Singh**

AI • Machine Learning • Data Science
""")

# ===================================================
# FOOTER
# ===================================================

st.divider()

st.caption(
    "🚀 AI Career Copilot • Developed by Shruti Singh"
)