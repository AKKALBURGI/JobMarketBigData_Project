import streamlit as st

from src.analytics import (
    create_spark,
    load_jobs,
    prepare_jobs,
    top_skills,
    jobs_by_role,
    jobs_by_location,
    average_salary_by_role
)

from src.questions import answer_question


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Job Market Skill Analytics",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# CREATE SPARK SESSION
# --------------------------------------------------

@st.cache_resource
def get_spark():
    return create_spark()


# --------------------------------------------------
# LOAD AND PREPARE DATA
# --------------------------------------------------

@st.cache_resource
def get_data():

    spark = get_spark()

    df = load_jobs(
        spark,
        "data/jobs.csv"
    )

    df = prepare_jobs(df)

    return df


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = get_data()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Job Market Skill Analytics")

st.write(
    "A mini Big Data project using PySpark to analyze "
    "100,000 synthetic job postings."
)


# --------------------------------------------------
# BASIC STATISTICS
# --------------------------------------------------

total_jobs = df.count()

total_locations = (
    df.select("location")
    .distinct()
    .count()
)

total_roles = (
    df.select("job_title")
    .distinct()
    .count()
)

total_skills = (
    df.selectExpr(
        "explode(skills_array) as skill"
    )
    .select("skill")
    .distinct()
    .count()
)


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Jobs",
    f"{total_jobs:,}"
)

col2.metric(
    "Locations",
    total_locations
)

col3.metric(
    "Job Roles",
    total_roles
)

col4.metric(
    "Unique Skills",
    total_skills
)


st.divider()


# --------------------------------------------------
# TOP SKILLS
# --------------------------------------------------

st.subheader("🔥 Top 10 Most Demanded Skills")

skills_df = top_skills(
    df,
    10
).toPandas()

st.bar_chart(
    skills_df.set_index("skill")["job_count"]
)


st.divider()


# --------------------------------------------------
# JOBS BY ROLE
# --------------------------------------------------

st.subheader("💼 Jobs by Role")

role_df = jobs_by_role(
    df
).toPandas()

st.bar_chart(
    role_df.set_index("job_title")["job_count"]
)


st.divider()


# --------------------------------------------------
# JOBS BY LOCATION
# --------------------------------------------------

st.subheader("📍 Jobs by Location")

location_df = jobs_by_location(
    df
).toPandas()

st.bar_chart(
    location_df.set_index("location")["job_count"]
)


st.divider()


# --------------------------------------------------
# AVERAGE SALARY
# --------------------------------------------------

st.subheader("💰 Average Salary by Role")

salary_df = average_salary_by_role(
    df
).toPandas()

st.dataframe(
    salary_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


# --------------------------------------------------
# QUESTION ANSWERING
# --------------------------------------------------

st.subheader("💬 Ask the Job Market")

question = st.text_input(
    "Ask a question about the job data:",
    placeholder="Example: What are the top skills?"
)


if st.button("Get Answer"):

    if question.strip():

        answer = answer_question(
            df,
            question
        )

        st.success(answer)

    else:

        st.warning(
            "Please enter a question."
        )


st.divider()


# --------------------------------------------------
# SAMPLE QUESTIONS
# --------------------------------------------------

st.subheader("Example Questions")

st.write(
    """
    • What are the top skills?

    • How many Data Engineer jobs are there?

    • What is the average salary for Data Analyst jobs?

    • Which location has the most jobs?

    • What is the total number of jobs?
    """
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Powered by Python, Apache Spark, PySpark and Streamlit"
)