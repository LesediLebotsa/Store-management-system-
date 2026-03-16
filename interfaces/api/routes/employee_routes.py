from flask import Blueprint
from services import store_service
from services.employee_service import EmployeeService

employee_routes = Blueprint("employees", __name__)




@employee_routes.route("/employees", methods=["GET"])
def get_employees():
    employee = EmployeeService.get_all_employees()
    try:

        formatted_employees = []

        for emp in employee:
            formatted_employees.append({
                "id": emp[0],
                "name": emp[1],
                "surname": emp[2],
                "phone": emp[3],
                "email": emp[4]
            })

        return {"employees": formatted_employees}

    except Exception as e:
        return {"error": str(e)}, 500