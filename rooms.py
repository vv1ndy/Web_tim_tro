from flask import Blueprint, request, jsonify
from models import get_room_collection

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route("/add-room", methods=["POST"])
def add_room():
    data = request.json
    rooms = get_room_collection()
    
    if "location" not in data or "lat" not in data["location"] or "lng" not in data["location"]:
        return jsonify({"message": "Vui lòng nhập vị trí hợp lệ"}), 400

    room_id = rooms.insert_one(data).inserted_id
    return jsonify({"message": "Thêm phòng thành công", "room_id": str(room_id)})

@rooms_bp.route("/get-rooms", methods=["GET"])
def get_rooms():
    rooms = list(get_room_collection().find({}, {"_id": 0}))
    return jsonify(rooms)

