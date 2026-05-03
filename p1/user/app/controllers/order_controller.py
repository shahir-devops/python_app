from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService
from app.validators.order_validator import validate_order

order_bp = Blueprint("order", __name__)
service = OrderService()

@order_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.json

    error = validate_order(data)
    if error:
        return {"error": error}, 400

    order = service.create_order(data)
    return jsonify(order), 201


@order_bp.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(service.get_orders())