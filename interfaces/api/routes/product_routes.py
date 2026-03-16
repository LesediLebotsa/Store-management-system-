from flask import Blueprint, jsonify, request
from services import store_service

product_routes = Blueprint("products", __name__)

@product_routes.route("/products", methods=["GET"])
def get_products():
    products = store_service.display_products()

    formatted_products = []

    for product in products:
        formatted_products.append({
            "id": product[0],
            "name": product[1],
            "price": product[2],
            "quantity": product[3]
        })

    return {"products": formatted_products}


@product_routes.route("/products", methods=["POST"])
def create_product():

    try:
        data = request.get_json()

        # check if request body exists
        if not data:
            return {"error": "Request body must contain data"}, 400

        # validate required fields
        required_fields = ["product_id", "name", "price", "quantity"]

        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 400

        product_id = data.get["product_id"]
        name = data.get["name"]
        price = data.get["price"]
        quantity = data.get["quantity"]

        store_service.add_product(product_id, name, price, quantity)

        return {"message": "Product created successfully"}, 201

    except Exception as e:
        return {"error":str(e)}, 500



@product_routes.route("/products/<int:product_id>/reduce", methods=["PATCH"])
def delete_product(product_id):

    data = request.json

    if not data or "amount" not in data:
        return {"error: Missing field: amount"}, 400

    amount = data["amount"]

    store_service.remove_product(product_id, amount)

    return {"message": f"Product {product_id} was successfully reduced by {amount}"}
