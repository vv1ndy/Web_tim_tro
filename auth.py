from flask import Blueprint, request, jsonify
import bcrypt
from models import get_user_collection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    users = get_user_collection()

    if users.find_one({"email": data["email"]}):
        return jsonify({"message": "Email đã tồn tại"}), 400

    hashed_pw = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    users.insert_one({"email": data["email"], "password": hashed_pw, "role": data["role"]})
    return jsonify({"message": "Đăng ký thành công"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    users = get_user_collection()

    user = users.find_one({"email": data["email"]})
    if user and bcrypt.checkpw(data["password"].encode(), user["password"]):
        return jsonify({"message": "Đăng nhập thành công"}), 200
    return jsonify({"message": "Sai thông tin đăng nhập"}), 401

