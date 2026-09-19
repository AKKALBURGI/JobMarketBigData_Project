from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    col,
    count,
    explode,
    split,
    trim,
    round
)


def create_spark():
    return (
        SparkSession.builder
        .appName("JobMarketSkillAnalytics")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )


def load_jobs(spark, path="data/jobs.csv"):
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(path)
    )


def prepare_jobs(df):
    return (
        df.dropna(
            subset=[
                "job_title",
                "location",
                "skills",
                "salary_lpa"
            ]
        )
        .dropDuplicates(["job_id"])
        .withColumn(
            "skills_array",
            split(col("skills"), ",\\s*")
        )
    )


def top_skills(df, n=10):
    return (
        df.select(
            explode("skills_array").alias("skill")
        )
        .withColumn(
            "skill",
            trim(col("skill"))
        )
        .filter(
            col("skill") != ""
        )
        .groupBy("skill")
        .agg(
            count("*").alias("job_count")
        )
        .orderBy(
            col("job_count").desc()
        )
        .limit(n)
    )


def jobs_by_role(df):
    return (
        df.groupBy("job_title")
        .agg(
            count("*").alias("job_count")
        )
        .orderBy(
            col("job_count").desc()
        )
    )


def jobs_by_location(df):
    return (
        df.groupBy("location")
        .agg(
            count("*").alias("job_count")
        )
        .orderBy(
            col("job_count").desc()
        )
    )


def average_salary_by_role(df):
    return (
        df.groupBy("job_title")
        .agg(
            round(
                avg("salary_lpa"),
                2
            ).alias("average_salary_lpa")
        )
        .orderBy(
            col("average_salary_lpa").desc()
        )
    )


def jobs_by_experience(df):
    return (
        df.groupBy("experience_years")
        .agg(
            count("*").alias("job_count")
        )
        .orderBy("experience_years")
    )


def stop_spark(spark):
    spark.stop()