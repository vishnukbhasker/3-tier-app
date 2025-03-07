<!-- backend/main.py -->
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Database connection
conn = mysql.connector.connect(
    host="db",
    user="root",
    password="password",
    database="users_db"
)
cursor = conn.cursor()

class User(BaseModel):
    name: str
    age: int

@app.post("/users/")
def add_user(user: User):
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (user.name, user.age))
    conn.commit()
    return {"message": "User added successfully"}

@app.get("/users/")
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return {"users": users}
