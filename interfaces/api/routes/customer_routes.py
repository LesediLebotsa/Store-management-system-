from flask import Blueprint
from services import store_service
from models.customer import Customer

customer_routes = Blueprint("customers", __name__)


@customer_routes.route("/customers", methods=["GET"])
def get_customers():

    try:
        customers = Customer.display_customers()

        formatted_customers = []

        for cust in customers:
            formatted_customers.append({
                "id": cust[0],
                "name": cust[1],
                "surname": cust[2],
                "phone": cust[3],
                "email": cust[4],
                "address": cust[5]
            })

        return {"customers": formatted_customers}

    except Exception as e:
        return {"error": str(e)}, 500