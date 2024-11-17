# models.py
from flask_pymongo import PyMongo
from datetime import datetime

mongo = PyMongo()

# User Model
def create_user(user_id, username, password, role="user"):
    return {
        "user_id": user_id,
        "username": username,
        "password": password,  # Hashed password
        "role": role,          # "user" or "admin"
        "created_at": datetime.utcnow()
    }

# Assignment Model
def create_assignment(user_id, task, admin_id=None):
    return {
        "user_id": user_id,
        "task": task,
        "admin_id": admin_id,
        "status": "pending",  # "pending", "accepted", "rejected"
        "created_at": datetime.utcnow()
    }
