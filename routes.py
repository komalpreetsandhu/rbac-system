from flask import jsonify
from models import User
from app import app

@app.route('/users/<username>/permissions')
def get_permissions(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    permissions = [p.name for p in user.role.permissions]

    return jsonify({
        "username": user.username,
        "role": user.role.name,
        "permissions": permissions
    })