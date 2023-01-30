FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingest_data.py ingest_data.py
# Source location -> target location

ENTRYPOINT [ "python", "ingest_data.py" ]