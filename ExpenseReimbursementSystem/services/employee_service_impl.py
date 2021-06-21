from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from services.employee_service import EmployeeService


class EmployeeServiceImpl(EmployeeService):

    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao = employee_dao

    def add_employee(self, employee: Employee):
        return self.employee_dao.create_employee(employee)

    def retrieve_all_employees(self):
        return self.employee_dao.get_all_employees()

    def retrieve_employee_by_id(self, employee_id: int):
        return self.employee_dao.get_employee(employee_id)

    def update_employee(self, employee: Employee):
        return self.employee_dao.update_employee(employee)

    def remove_employee(self, employee_id: int):
        return self.employee_dao.delete_employee(employee_id)
