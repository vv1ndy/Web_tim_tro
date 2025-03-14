# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from routes.rooms import rooms_bp

app = Flask(__name__)

# Kết nối MongoDB (sử dụng database 'phongtro')
app.config["MONGO_URI"] = "mongodb://localhost:27017/phongtro"
mongo = PyMongo(app)

# Đăng ký route quản lý phòng trọ
app.register_blueprint(rooms_bp)

@app.route("/")
def home():
    return "Server Flask đang chạy!"

if __name__ == "__main__":
    app.run(debug=True)

