from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "supersecretkey"  # Change this to a proper secret key
jwt = JWTManager(app)

# Dummy users database
users_db = {
    "soumik": {"password": "password123", "role": "user"},
    "alok": {"password": "adminpassword", "role": "admin"}
}

# Register user endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users_db:
        return jsonify({"message": "User already exists!"}), 400
    
    users_db[username] = {"password": password, "role": "user"}
    return jsonify({"message": "User registered successfully!"}), 201

# Login user endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = users_db.get(username)
    if not user or user['password'] != password:
        return jsonify({"message": "Invalid credentials!"}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Upload assignment (only users can upload)
@app.route('/upload', methods=['POST'])
@jwt_required()
def upload_assignment():
    current_user = get_jwt_identity()
    data = request.get_json()
    task = data.get('task')
    
    if not task:
        return jsonify({"message": "Task is required!"}), 400
    
    # You can save assignments to a database or just print for now
    print(f"Assignment from {current_user}: {task}")
    return jsonify({"message": "Assignment uploaded successfully!"}), 201

# Admin route to view assignments (dummy implementation)
@app.route('/assignments', methods=['GET'])
@jwt_required()
def view_assignments():
    current_user = get_jwt_identity()
    user = users_db.get(current_user)
    
    if not user or user['role'] != "admin":
        return jsonify({"message": "Admin access required!"}), 403
    
    # For demo purposes, we are simply printing a dummy assignment list
    assignments = [{"user": "soumik", "task": "Hello World Assignment", "status": "pending"}]
    return jsonify(assignments), 200

# Accept assignment (admin only)
@app.route('/assignments/<string:id>/accept', methods=['POST'])
@jwt_required()
def accept_assignment(id):
    current_user = get_jwt_identity()
    user = users_db.get(current_user)
    
    if not user or user['role'] != "admin":
        return jsonify({"message": "Admin access required!"}), 403
    
    return jsonify({"message": f"Assignment {id} accepted!"}), 200

# Reject assignment (admin only)
@app.route('/assignments/<string:id>/reject', methods=['POST'])
@jwt_required()
def reject_assignment(id):
    current_user = get_jwt_identity()
    user = users_db.get(current_user)
    
    if not user or user['role'] != "admin":
        return jsonify({"message": "Admin access required!"}), 403
    
    return jsonify({"message": f"Assignment {id} rejected!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
