from flask import Flask, request
from interfaces.api.routes.product_routes import product_routes
from interfaces.api.routes.employee_routes import employee_routes
from interfaces.api.routes.customer_routes import customer_routes
from interfaces.api.routes.sales_routes import sales_routes
from flasgger import Swagger

def create_app(test_config=None):
    app = Flask(__name__)
    Swagger(app)

    if test_config:
        app.config.update(test_config)


    app.register_blueprint(product_routes)
    app.register_blueprint(employee_routes)
    app.register_blueprint(customer_routes)
    app.register_blueprint(sales_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

