from flask import Blueprint, jsonify

# Create a Blueprint instance
user_blueprint = Blueprint('user', __name__)

# Define routes associated with this Blueprint
@user_blueprint.route('/api/v1/users', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return jsonify(users)

@user_blueprint.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = {"id": user_id, "name": f"User {user_id}"}
    return jsonify(user)
