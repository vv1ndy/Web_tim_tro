from flask_pymongo import PyMongo
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cấu hình MongoDB (sửa nếu dùng MongoDB Atlas)
app.config["MONGO_URI"] = "mongodb://localhost:27017/room_management"
mongo = PyMongo(app)

