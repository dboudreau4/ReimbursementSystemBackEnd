from typing import List

from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from utils.connection_util import connection


class EmployeeDAOPostgres(EmployeeDAO):

    def create_employee(self, employee: Employee) -> Employee:
        sql = """insert into employee (first_name, last_name, username, pass) values (%s, %s, %s, %s) returning 
        employee_id """
        cursor = connection.cursor()
        cursor.execute(sql, (employee.first_name, employee.last_name, employee.username, employee.password))
        connection.commit()
        employee_id = cursor.fetchone()[0]
        employee.employee_id = employee_id
        return employee

    def get_employee(self, employee_id: int) -> Employee:
        sql = """select * from employee where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        employee = Employee(*record)
        return employee

    def get_all_employees(self) -> List[Employee]:
        sql = """select * from employee"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employee_list = []
        for record in records:
            employee_list.append(Employee(*record))
        return employee_list

    def update_employee(self, employee: Employee) -> Employee:
        sql = """update employee set first_name=%s, last_name=%s, username=%s, pass=%s where employee_id =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee.first_name, employee.last_name, employee.username, employee.password, employee.employee_id))
        connection.commit()
        return employee

    def delete_employee(self, employee_id: int) -> bool:
        sql = """delete from employee where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        return True
