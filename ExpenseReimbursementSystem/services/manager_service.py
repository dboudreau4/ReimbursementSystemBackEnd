from abc import ABC, abstractmethod

from entities.manager import Manager


class ManagerService(ABC):

    @abstractmethod
    def add_manager(self, manager: Manager):
        pass

    @abstractmethod
    def retrieve_all_managers(self):
        pass

    @abstractmethod
    def retrieve_manager_by_id(self, manager_id: int):
        pass

    @abstractmethod
    def update_manager(self, manager: Manager):
        pass

    @abstractmethod
    def remove_manager(self, manager_id: int):
        pass
