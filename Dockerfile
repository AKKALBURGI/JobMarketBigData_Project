FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends default-jre \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD streamlit run app.py --server.address 0.0.0.0 --server.port ${PORT:-10000}