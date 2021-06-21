from daos.manager_dao import ManagerDAO
from daos.manager_dao_postgres import ManagerDAOPostgres
from entities.manager import Manager

manager_dao: ManagerDAO = ManagerDAOPostgres()

test_manager = Manager(0, "Murali", "Durgiah", "mdurgiah", "pass")


def test_create_manager():
    manager_dao.create_manager(test_manager)
    assert test_manager.manager_id != 0


def test_get_manager():
    manager = manager_dao.get_manager(test_manager.manager_id)
    assert test_manager.manager_id == manager.manager_id


def test_get_all_managers():
    manager1 = Manager(0, "Brittany", "Durgiah", "bdurgiah", "pass")
    manager2 = Manager(0, "Janaki", "Ross", "jross", "pass")
    manager3 = Manager(0, "Kaitlen", "Ross", "kross", "pass")
    manager_dao.create_manager(manager1)
    manager_dao.create_manager(manager2)
    manager_dao.create_manager(manager3)
    managers = manager_dao.get_all_managers()
    assert len(managers) >= 3


def test_update_manager():
    test_manager.first_name = "John"
    updated_manager = manager_dao.update_manager(test_manager)
    assert updated_manager.first_name == test_manager.first_name


def test_delete_manager():
    result = manager_dao.delete_manager(test_manager.manager_id)
    assert result
