import csv
import random
import os
from datetime import date, timedelta
from faker import Faker

fake = Faker("en_IN")

OUTPUT = "data/jobs.csv"
NUM_RECORDS = 100_000

job_roles = {
    "Data Analyst": [
        "Python", "SQL", "Excel", "Power BI", "Tableau", "Statistics"
    ],
    "Data Engineer": [
        "Python", "SQL", "Spark", "Kafka", "AWS", "Docker", "Hadoop"
    ],
    "ML Engineer": [
        "Python", "Machine Learning", "TensorFlow",
        "PyTorch", "SQL", "Docker"
    ],
    "Software Engineer": [
        "Python", "Java", "C++", "Git", "Docker", "AWS", "SQL"
    ],
    "Cloud Engineer": [
        "AWS", "Azure", "Docker", "Kubernetes",
        "Linux", "Python", "Terraform"
    ],
    "DevOps Engineer": [
        "AWS", "Docker", "Kubernetes", "Jenkins",
        "Linux", "Terraform", "Git"
    ],
    "AI Engineer": [
        "Python", "Machine Learning", "Deep Learning",
        "TensorFlow", "PyTorch", "SQL", "LLM"
    ],
    "Business Analyst": [
        "SQL", "Excel", "Power BI",
        "Tableau", "Statistics", "Communication"
    ],
}

locations = [
    "Bengaluru", "Hyderabad", "Pune", "Mumbai",
    "Chennai", "Delhi", "Noida", "Gurugram",
    "Kolkata", "Ahmedabad", "Kochi",
    "Mysuru", "Hubballi"
]

experience_levels = [0, 1, 2, 3, 4, 5, 6, 7, 8]

salary_base = {
    "Data Analyst": 5.5,
    "Data Engineer": 8.5,
    "ML Engineer": 9.5,
    "Software Engineer": 7.0,
    "Cloud Engineer": 8.0,
    "DevOps Engineer": 8.0,
    "AI Engineer": 10.0,
    "Business Analyst": 6.0,
}

job_descriptions = {
    "Data Analyst": (
        "We are looking for a Data Analyst with experience in {skills}. "
        "The candidate will analyze business data, prepare reports, "
        "identify trends, and create dashboards to support business decisions."
    ),

    "Data Engineer": (
        "We are looking for a Data Engineer with experience in {skills}. "
        "The candidate will build data pipelines, process large datasets, "
        "and develop reliable data solutions for analytics."
    ),

    "ML Engineer": (
        "We are looking for an ML Engineer with experience in {skills}. "
        "The candidate will develop, test, and deploy machine learning models "
        "and work with data science teams on practical AI solutions."
    ),

    "Software Engineer": (
        "We are looking for a Software Engineer with experience in {skills}. "
        "The candidate will design, develop, test, and maintain software "
        "applications while working with a collaborative engineering team."
    ),

    "Cloud Engineer": (
        "We are looking for a Cloud Engineer with experience in {skills}. "
        "The candidate will design and maintain cloud infrastructure, "
        "improve system reliability, and support scalable applications."
    ),

    "DevOps Engineer": (
        "We are looking for a DevOps Engineer with experience in {skills}. "
        "The candidate will automate deployment processes, manage infrastructure, "
        "and improve the reliability of software delivery pipelines."
    ),

    "AI Engineer": (
        "We are looking for an AI Engineer with experience in {skills}. "
        "The candidate will develop AI solutions, work with machine learning "
        "models, and integrate intelligent features into applications."
    ),

    "Business Analyst": (
        "We are looking for a Business Analyst with experience in {skills}. "
        "The candidate will analyze business requirements, prepare reports, "
        "and work with technical teams to improve business processes."
    ),
}


def make_salary(role, experience):
    base = salary_base[role]

    salary = (
        base
        + experience * random.uniform(0.45, 0.9)
        + random.uniform(-0.7, 1.5)
    )

    return round(max(salary, 3.0), 1)


def make_posted_date():
    days_ago = random.randint(0, 365)
    return date.today() - timedelta(days=days_ago)


def main():

    os.makedirs("data", exist_ok=True)

    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "job_id",
            "job_title",
            "company",
            "location",
            "skills",
            "experience_years",
            "salary_lpa",
            "posted_date",
            "job_description"
        ])

        for i in range(1, NUM_RECORDS + 1):

            # Select a job role
            role = random.choice(list(job_roles.keys()))

            # Select skills related to that role
            available_skills = job_roles[role]

            skill_count = random.randint(
                3,
                min(6, len(available_skills))
            )

            skills = random.sample(
                available_skills,
                skill_count
            )

            # Generate experience and salary
            experience = random.choice(experience_levels)
            salary = make_salary(role, experience)

            # Faker generates a synthetic company name
            company = fake.company()

            # Select location
            location = random.choice(locations)

            # Generate a date within the last year
            posted_date = make_posted_date()

            # Generate meaningful English description
            description = job_descriptions[role].format(
                skills=", ".join(skills)
            )

            writer.writerow([
                i,
                role,
                company,
                location,
                ", ".join(skills),
                experience,
                salary,
                posted_date,
                description
            ])

    print(f"Created {NUM_RECORDS:,} records at {OUTPUT}")


if __name__ == "__main__":
    main()