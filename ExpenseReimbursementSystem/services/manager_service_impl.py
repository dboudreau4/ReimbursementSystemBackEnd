from daos.manager_dao import ManagerDAO
from entities.manager import Manager
from services.manager_service import ManagerService


class ManagerServiceImpl(ManagerService):

    def __init__(self, manager_dao: ManagerDAO):
        self.manager_dao = manager_dao

    def add_manager(self, manager: Manager):
        return self.manager_dao.create_manager(manager)

    def retrieve_all_managers(self):
        return self.manager_dao.get_all_managers()

    def retrieve_manager_by_id(self, manager_id: int):
        return self.manager_dao.get_manager(manager_id)

    def update_manager(self, manager: Manager):
        return self.manager_dao.update_manager(manager)

    def remove_manager(self, manager_id: int):
        return self.manager_dao.delete_manager(manager_id)