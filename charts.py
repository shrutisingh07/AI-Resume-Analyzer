import pandas as pd
import streamlit as st

def show_skill_chart(resume_skills, missing_skills):

    labels = ["Skills Found", "Missing Skills"]

    values = [len(resume_skills), len(missing_skills)]

    df = pd.DataFrame({
        "Category": labels,
        "Count": values
    })

    st.bar_chart(
        df.set_index("Category")
    )