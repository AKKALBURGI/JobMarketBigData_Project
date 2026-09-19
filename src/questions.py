from pyspark.sql.functions import col, count, explode, trim, avg

def answer_question(df, question):
    q = question.lower().strip()

    if "top" in q and "skill" in q:
        result = (
            df.select(explode("skills_array").alias("skill"))
              .withColumn("skill", trim(col("skill")))
              .groupBy("skill")
              .agg(count("*").alias("job_count"))
              .orderBy(col("job_count").desc())
              .limit(5)
              .collect()
        )
        return "Top 5 skills:\n" + "\n".join(
            f"{i+1}. {r['skill']} — {r['job_count']:,} job postings"
            for i, r in enumerate(result)
        )

    role = next((r for r in [
        "Data Analyst", "Data Engineer", "ML Engineer", "Software Engineer",
        "Cloud Engineer", "DevOps Engineer", "AI Engineer", "Business Analyst"
    ] if r.lower() in q), None)

    if "how many" in q and role:
        n = df.filter(col("job_title") == role).count()
        return f"{role} job postings: {n:,}"

    if "average salary" in q and role:
        row = (
            df.filter(col("job_title") == role)
              .select(avg("salary_lpa").alias("avg"))
              .first()
        )
        return f"Average salary for {role}: ₹{row['avg']:.2f} LPA"

    if "location" in q and ("most" in q or "highest" in q):
        row = (
            df.groupBy("location")
              .agg(count("*").alias("job_count"))
              .orderBy(col("job_count").desc())
              .first()
        )
        return f"Location with the most job postings: {row['location']} ({row['job_count']:,})"

    if "total" in q and "job" in q:
        return f"Total job postings: {df.count():,}"

    return (
        "I can answer questions such as:\n"
        "• What are the top skills?\n"
        "• How many Data Engineer jobs are there?\n"
        "• What is the average salary for Data Analyst jobs?\n"
        "• Which location has the most jobs?\n"
        "• What is the total number of jobs?"
    )
