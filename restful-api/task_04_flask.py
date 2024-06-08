#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    if username:
        users[username] = {
            "username": username,
            "name": data.get('name'),
            "age": data.get('age'),
            "city": data.get('city')
        }
        return jsonify({"message": "User added", "user": users[username]})
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True)

