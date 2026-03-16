from flask import Blueprint, request
from services import store_service

sales_routes = Blueprint("sales", __name__)

@sales_routes.route("/sales", methods=["POST"])
def create_sale():

    try:
        data = request.json

        if not data:
            return {"error": "Request body must contain JSON"}, 400

        required_fields = ["product_id", "name", "price", "quantity"]

        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 400

        product_id = data["product_id"]
        name = data["name"]
        price = data["price"]
        quantity = data["quantity"]

        store_service.sell_product(product_id, name, price, quantity)

        return {"message": "Sale completed successfully"}, 201

    except Exception as e:
        return {"error": str(e)}, 500