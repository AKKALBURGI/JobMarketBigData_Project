# Job Market Skill Analytics using PySpark

A beginner-friendly Big Data mini-project that processes a large job-posting dataset with Apache Spark/PySpark and provides analytics plus a simple question-answer interface.

## Features

- Generate 100,000 synthetic job postings
- Process data using PySpark
- Analyze top skills
- Analyze jobs by role
- Analyze jobs by location
- Calculate average salary by role
- Ask simple questions about the dataset
- View results in a Streamlit dashboard

## Technology Stack

- Python
- Apache Spark
- PySpark
- Streamlit
- Pandas
- Faker

## Project Structure

```text
JobMarketBigData/
├── data/
│   └── jobs.csv
├── src/
│   ├── generate_data.py
│   ├── analytics.py
│   └── questions.py
├── app.py
├── requirements.txt
└── README.md
```

## How to Run

### 1. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the dataset

From the project root:

```bash
python src/generate_data.py
```

This creates:

```text
data/jobs.csv
```

with 100,000 job records.

### 4. Start the dashboard

```bash
streamlit run app.py
```

The browser should open the dashboard.

## Example Questions

- What are the top skills?
- How many Data Engineer jobs are there?
- What is the average salary for Data Analyst jobs?
- Which location has the most jobs?
- What is the total number of jobs?

## Big Data Concept

The project uses Apache Spark for large-scale data processing. PySpark is the Python API for Apache Spark. The project demonstrates Spark DataFrames, transformations, grouping, aggregation, and distributed-style processing.

The generated dataset is synthetic and is intended for academic demonstration. Salary and skill statistics are not real labor-market measurements.
