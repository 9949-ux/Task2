from flask import Blueprint, jsonify, request
from models import inventory, find_item, update_item, delete_item

inventory_bp = Blueprint('inventory_bp', __name__)

@inventory_bp.route("/", methods=["GET"])
def get_items():
    return jsonify(inventory)

@inventory_bp.route("/<string:item_id>", methods=["GET"])
def get_item(item_id):
    item = find_item(item_id)
    return jsonify(item) if item else ("Item not found", 404)

@inventory_bp.route("/", methods=["POST"])
def add_item():
    data = request.get_json()
    inventory.append(data)
    return jsonify({"message": "Item added", "item": data}), 201

@inventory_bp.route("/<string:item_id>", methods=["PUT"])
def edit_item(item_id):
    data = request.get_json()
    updated = update_item(item_id, data)
    return jsonify(updated) if updated else ("Item not found", 404)

@inventory_bp.route("/<string:item_id>", methods=["DELETE"])
def remove_item(item_id):
    removed = delete_item(item_id)
    return jsonify(removed) if removed else ("Item not found", 404)
