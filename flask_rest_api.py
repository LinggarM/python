from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run()