from typing import List

from daos.manager_dao import ManagerDAO
from entities.manager import Manager
from utils.connection_util import connection


class ManagerDAOPostgres(ManagerDAO):

    def create_manager(self, manager: Manager) -> Manager:
        sql = """insert into manager (first_name, last_name, username, pass) values (%s, %s, %s, %s) returning 
        manager_id """
        cursor = connection.cursor()
        cursor.execute(sql, (manager.first_name, manager.last_name, manager.username, manager.password))
        connection.commit()
        manager_id = cursor.fetchone()[0]
        manager.manager_id = manager_id
        return manager

    def get_manager(self, manager_id: int) -> Manager:
        sql = """select * from manager where manager_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        record = cursor.fetchone()
        manager = Manager(*record)
        return manager

    def get_all_managers(self) -> List[Manager]:
        sql = """select * from manager"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        manager_list = []
        for record in records:
            manager_list.append(Manager(*record))
        return manager_list

    def update_manager(self, manager: Manager) -> Manager:
        sql = """update manager set first_name=%s, last_name=%s, username=%s, pass=%s where manager_id =%s"""
        cursor = connection.cursor()
        cursor.execute(sql, (manager.first_name, manager.last_name, manager.username, manager.password, manager.manager_id))
        connection.commit()
        return manager

    def delete_manager(self, manager_id: int) -> bool:
        sql = """delete from manager where manager_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        connection.commit()
        return True
