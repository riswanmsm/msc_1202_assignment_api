from flask import Flask, request, jsonify
import hashlib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set up a user database with some test users
users = {
    'Riswan': hashlib.sha256('password123'.encode('utf-8')).hexdigest(),
    'Saman': hashlib.sha256('pass123'.encode('utf-8')).hexdigest(),
    'Lahiru': hashlib.sha256('qwerty123'.encode('utf-8')).hexdigest()
}

# Define a route to handle authentication requests


@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Get the username and password from the request body
    username = request.json['username']
    password = request.json['password']

    # Check if the username is in the user database
    if username in users:
        # Hash the provided password and compare it to the stored hash
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if password_hash == users[username]:
            # Authentication successful, return a success response
            return jsonify({'authenticated': True}), 200
        else:
            # Incorrect password, return an error response
            return jsonify({'error': 'Incorrect password'}), 401
    else:
        # User not found, return an error response
        return jsonify({'error': 'User not found'}), 401


if __name__ == '__main__':
    app.run(debug=True)
