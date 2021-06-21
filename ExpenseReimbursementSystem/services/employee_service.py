from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeService(ABC):

    @abstractmethod
    def add_employee(self, employee: Employee):
        pass

    @abstractmethod
    def retrieve_all_employees(self):
        pass

    @abstractmethod
    def retrieve_employee_by_id(self, employee_id: int):
        pass

    @abstractmethod
    def update_employee(self, employee: Employee):
        pass

    @abstractmethod
    def remove_employee(self, employee_id: int):
        pass

