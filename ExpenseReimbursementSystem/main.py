import logging

from flask import Flask, jsonify, request
from flask_cors import CORS

from daos.employee_dao_postgres import EmployeeDAOPostgres
from daos.manager_dao_postgres import ManagerDAOPostgres
from daos.reimbursement_request_dao_postgres import ReimbursementRequestDAOPostgres
from entities.reimbursement_request import ReimbursementRequest
from services.employee_service_impl import EmployeeServiceImpl
from services.manager_service_impl import ManagerServiceImpl
from services.reimbursement_request_service_impl import ReimbursementRequestServiceImpl

app = Flask = Flask(__name__)
CORS(app)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')

employee_dao = EmployeeDAOPostgres()
employee_service = EmployeeServiceImpl(employee_dao)

manager_dao = ManagerDAOPostgres()
manager_service = ManagerServiceImpl(manager_dao)

reimbursement_request_dao = ReimbursementRequestDAOPostgres()
request_service = ReimbursementRequestServiceImpl(reimbursement_request_dao)


# ------------------------------ EMPLOYEES ----------------------------------- #

@app.route("/ERS/employees", methods=["GET"])
def get_all_employees():
    employees = employee_service.retrieve_all_employees()
    json_employees = [e.as_json_dict() for e in employees]
    return jsonify(json_employees), 200


@app.route("/ERS/employees/<employee_id>", methods=["GET"])
def get_employee(employee_id: str):
    try:
        employee = employee_service.retrieve_employee_by_id(int(employee_id))
        return employee.as_json_dict(), 200
    except TypeError:
        return f"The employee with id {employee_id} does not exist", 404


@app.route("/ERS/employees/<employee_id>/requests", methods=["GET"])
def get_all_employee_requests(employee_id: str):
    try:
        employee = employee_service.retrieve_employee_by_id(int(employee_id))
    except TypeError:
        return f"The employee with id {employee_id} does not exist", 404

    employee_requests = []
    requests = request_service.retrieve_all_reimbursement_requests()

    for r in requests:
        if r.employee_id == int(employee_id):
            employee_requests.append(r.as_json_dict())
    return jsonify(employee_requests), 200


@app.route("/ERS/employees/<employee_id>/requests", methods=["POST"])
def create_employee_request(employee_id: str):
    body = request.json
    reimbursement_request = ReimbursementRequest(body["requestId"], body["employeeId"], body["amount"], body["reason"],
                                                 body["approved"], body["managerId"], body["message"])
    try:
        employee = employee_service.retrieve_employee_by_id(int(employee_id))
        reimbursement_request.employee_id = int(employee_id)
        reimbursement_request.status = "pending"
        reimbursement_request.manager_id = 1  # default assigned to manager_id 1
        reimbursement_request.message = ""
        request_service.add_reimbursement_request(reimbursement_request)
        return reimbursement_request.as_json_dict(), 201
    except TypeError:
        return f"The employee with id {employee_id} does not exist", 404


# ------------------------------ MANAGERS ----------------------------------- #

@app.route("/ERS/managers", methods=["GET"])
def get_all_managers():
    managers = manager_service.retrieve_all_managers()
    json_managers = [m.as_json_dict() for m in managers]
    return jsonify(json_managers), 200


@app.route("/ERS/managers/requests", methods=["GET"])
def get_all_requests():
    requests = request_service.retrieve_all_reimbursement_requests()
    json_requests = [r.as_json_dict() for r in requests]
    return jsonify(json_requests), 200


@app.route("/ERS/managers/requests/<request_id>", methods=["GET"])
def get_request(request_id: str):
    try:
        reimbursement_request = request_service.retrieve_reimbursement_request_by_id(int(request_id))
        return reimbursement_request.as_json_dict(), 200
    except TypeError:
        return f"The account {request_id} doesn't exist", 404


@app.route("/ERS/managers/requests/<request_id>", methods=["PUT"])
def update_request(request_id: str):
    body = request.json
    updated_request = ReimbursementRequest(body["requestId"], body["employeeId"], body["amount"], body["reason"],
                                           body["approved"], body["managerId"], body["message"])
    updated_request.request_id = int(request_id)

    try:
        reimbursement_request = request_service.retrieve_reimbursement_request_by_id(int(request_id))
        request_service.update_reimbursement_request(updated_request)
        return updated_request.as_json_dict(), 205
    except TypeError:
        return f"The account {request_id} doesn't exist", 404


if __name__ == '__main__':
    app.run()
