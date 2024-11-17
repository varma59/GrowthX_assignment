Assignment Submission Portal
Overview
This is a backend system for an Assignment Submission Portal where Users can upload assignments, and Admins can review, accept, or reject assignments. The system is built using Flask and MongoDB for storage.

Key Features:
Users can register, log in, and upload assignments.
Admins can register, log in, view, accept, or reject assignments.
Prerequisites
Python 3.x installed on your machine.
MongoDB installed or use a cloud MongoDB service (e.g., MongoDB Atlas).
Postman to test the API (or you can use cURL).
Setup
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-repo/assignment-portal.git
cd assignment-portal
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your MongoDB database (either locally or via MongoDB Atlas). Update the MongoDB URI in app.py if needed.

Run the Flask app:

bash
Copy code
python app.py
The app will run on http://127.0.0.1:5000/.

Testing the API using Postman
1. Register a User
Method: POST

Endpoint: http://127.0.0.1:5000/register

Request Body:

json
Copy code
{
  "username": "soumik",
  "password": "password123"
}
Expected Response:

json
Copy code
{
  "message": "User registered successfully!"
}
2. Login a User
Method: POST

Endpoint: http://127.0.0.1:5000/login

Request Body:

json
Copy code
{
  "username": "soumik",
  "password": "password123"
}
Expected Response:

json
Copy code
{
  "access_token": "<your_jwt_token>"
}
3. Upload Assignment
Method: POST

Endpoint: http://127.0.0.1:5000/upload

Request Header: Authorization: Bearer <your_jwt_token>

Request Body:

json
Copy code
{
  "task": "Hello World Assignment"
}
Expected Response:

json
Copy code
{
  "message": "Assignment uploaded successfully!"
}
4. View Assignments (Admin Only)
Method: GET

Endpoint: http://127.0.0.1:5000/assignments

Request Header: Authorization: Bearer <admin_jwt_token>

Expected Response:

json
Copy code
[
  {
    "user": "soumik",
    "task": "Hello World Assignment",
    "status": "pending"
  }
]
5. Accept Assignment (Admin Only)
Method: POST

Endpoint: http://127.0.0.1:5000/assignments/1/accept

Request Header: Authorization: Bearer <admin_jwt_token>

Expected Response:

json
Copy code
{
  "message": "Assignment 1 accepted!"
}
6. Reject Assignment (Admin Only)
Method: POST

Endpoint: http://127.0.0.1:5000/assignments/1/reject

Request Header: Authorization: Bearer <admin_jwt_token>

Expected Response:

json
Copy code
{
  "message": "Assignment 1 rejected!"
}
Database Information
The project uses MongoDB to store users, assignments, and their statuses.
You do not need to include the database in the repository; the system will automatically interact with MongoDB once you set up the connection string in app.py (change the MongoDB URI to your database's URI).