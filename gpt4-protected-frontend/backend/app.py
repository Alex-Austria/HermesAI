from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USERS = {
    "user1": "password123",
    "user2": "mypassword"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if USERS.get(username) == password:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/gpt', methods=['POST'])
def gpt():
    # Hier würde die Logik für die GPT-4-ähnliche Anwendung eingefügt werden
    return jsonify({"response": "This is a GPT-4-like response"})

if __name__ == '__main__':
    app.run(debug=True)
