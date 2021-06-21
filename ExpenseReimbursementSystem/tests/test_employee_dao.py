from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDAOPostgres
from entities.employee import Employee

employee_dao: EmployeeDAO = EmployeeDAOPostgres()

test_employee = Employee(0, "Steph", "Ross", "sross", "pass")


def test_create_employee():
    employee_dao.create_employee(test_employee)
    assert test_employee.employee_id != 0


def test_get_employee():
    employee = employee_dao.get_employee(test_employee.employee_id)
    assert test_employee.employee_id == employee.employee_id


def test_get_all_employees():
    employee1 = Employee(0, "Josh", "Ross", "joshross", "pass")
    employee2 = Employee(0, "Janaki", "Ross", "jross", "pass")
    employee3 = Employee(0, "Kaitlen", "Ross", "kross", "pass")
    employee_dao.create_employee(employee1)
    employee_dao.create_employee(employee2)
    employee_dao.create_employee(employee3)
    employees = employee_dao.get_all_employees()
    assert len(employees) >= 3


def test_update_employee():
    test_employee.first_name = "John"
    updated_employee = employee_dao.update_employee(test_employee)
    assert updated_employee.first_name == test_employee.first_name


def test_delete_employee():
    result = employee_dao.delete_employee(test_employee.employee_id)
    assert result
