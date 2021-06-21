from abc import ABC, abstractmethod
from typing import List

from entities.employee import Employee


class EmployeeDAO(ABC):

    @abstractmethod
    def create_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_employee(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Employee]:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def delete_employee(self, employee_id: int) -> bool:
        pass

