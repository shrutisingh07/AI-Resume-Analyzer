# ==========================
# AI CAREER COPILOT MODULE
# ==========================

from skills import ROLE_SKILLS

# --------------------------
# Resume Feedback
# --------------------------

def generate_resume_feedback(ats_score, missing_skills):

    feedback = []

    if ats_score >= 85:
        feedback.append("Excellent ATS score. Your resume is highly competitive.")

    elif ats_score >= 70:
        feedback.append("Good ATS score. A few improvements can make your resume stronger.")

    else:
        feedback.append("Your resume needs improvement to pass ATS screening.")

    if missing_skills:

        feedback.append(
            "Add these important skills: "
            + ", ".join(missing_skills[:5])
        )

    feedback.append("Include measurable achievements.")

    feedback.append("Keep your resume to one page if possible.")

    feedback.append("Add GitHub and LinkedIn profile links.")

    return feedback


# --------------------------
# Skill Gap Analysis
# --------------------------

def skill_gap_analysis(job_role, resume_skills):

    required = ROLE_SKILLS.get(job_role, [])

    gaps = []

    for skill in required:

        if skill.lower() not in [s.lower() for s in resume_skills]:

            gaps.append(skill)

    return gaps


# --------------------------
# Learning Roadmap
# --------------------------

def learning_roadmap(gaps):

    roadmap = []

    week = 1

    for skill in gaps:

        roadmap.append(f"Week {week}: Learn {skill}")

        week += 1

    return roadmap


# --------------------------
# Interview Questions
# --------------------------

INTERVIEW_QUESTIONS = {

    "Data Analyst":[
        "Explain SQL JOINs.",
        "Difference between INNER and LEFT JOIN?",
        "What is normalization?",
        "Explain Pandas DataFrame.",
        "Difference between Power BI and Tableau?"
    ],

    "Data Scientist":[
        "Explain bias vs variance.",
        "What is overfitting?",
        "Difference between Random Forest and XGBoost?",
        "Explain Logistic Regression.",
        "How do you evaluate ML models?"
    ],

    "Machine Learning Engineer":[
        "What is MLOps?",
        "Explain TensorFlow.",
        "Difference between CNN and RNN.",
        "What is model deployment?",
        "Explain Docker."
    ],

    "AI Engineer":[
        "What is NLP?",
        "What are LLMs?",
        "Explain Transformers.",
        "Difference between BERT and GPT?",
        "What is Fine-tuning?"
    ],

    "Software Engineer":[
        "Explain OOP.",
        "Difference between Stack and Queue.",
        "Explain Git branching.",
        "What is Big O?",
        "Explain REST APIs."
    ]

}


def get_interview_questions(role):

    return INTERVIEW_QUESTIONS.get(role, [])


# --------------------------
# Project Recommendations
# --------------------------

PROJECTS = {

    "Data Analyst":[
        "Sales Dashboard",
        "Customer Segmentation",
        "Netflix Data Analysis"
    ],

    "Data Scientist":[
        "House Price Prediction",
        "Customer Churn Prediction",
        "Fraud Detection"
    ],

    "Machine Learning Engineer":[
        "Image Classifier",
        "MLOps Pipeline",
        "Recommendation System"
    ],

    "AI Engineer":[
        "AI Career Copilot",
        "Voice-to-SQL Generator",
        "LLM Chatbot"
    ],

    "Software Engineer":[
        "Library Management System",
        "Chat Application",
        "Task Manager"
    ]

}


def recommended_projects(role):

    return PROJECTS.get(role, [])