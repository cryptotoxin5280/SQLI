import mysql.connector
import os
from fastapi import FastAPI

app = FastAPI()

# Get DB config from environment variables.
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "sql_injection_demo")
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.post("/login")
async def login(username: str, password: str):

    conn = get_db_connection()
    cursor = conn.cursor()

    # Vulnerable SQL Query
    # query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    # cursor.execute(query)

    # Safe SQL Query (using a Parameterized Query)
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    if user:
        return {
            "message": "Login Successful!"
        }
    else:
        return {
            "message": "Invalid Credentials!"
        }