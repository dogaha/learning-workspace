import os
import psycopg
import pandas as pd
from dotenv import load_dotenv

load_dotenv() # load .env into environment variables

conn = psycopg.connect(
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD")
)

df = pd.read_sql_query("SELECT * FROM silver.politicians", conn)

conn.close()

print(df.head)