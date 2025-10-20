#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    """Root endpoint - returns welcome message"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Returns OK status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns user data for a specific username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the users dictionary"""
    # Check if request body is valid JSON
    try:
        user_data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    # If get_json() returns None, it means invalid JSON or wrong Content-Type
    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is provided
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to the dictionary
    users[username] = user_data

    # Return success response with 201 status code
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run()
