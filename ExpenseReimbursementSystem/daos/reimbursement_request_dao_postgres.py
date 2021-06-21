from typing import List

from daos.reimbursement_request_dao import ReimbursementRequestDAO
from entities.reimbursement_request import ReimbursementRequest
from utils.connection_util import connection


class ReimbursementRequestDAOPostgres(ReimbursementRequestDAO):
    def create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        sql = """insert into reimbursement_request (e_id, amount, reason, status, m_id, message) values (%s, %s, %s, %s, 
        %s, %s) returning request_id """
        cursor = connection.cursor()
        cursor.execute(sql,
                       (reimbursement_request.employee_id, reimbursement_request.amount, reimbursement_request.reason,
                        reimbursement_request.status, reimbursement_request.manager_id, reimbursement_request.message))
        connection.commit()
        request_id = cursor.fetchone()[0]
        reimbursement_request.request_id = request_id
        return reimbursement_request

    def get_reimbursement_request(self, reimbursement_request_id: int) -> ReimbursementRequest:
        sql = """select * from reimbursement_request where request_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_request_id])
        record = cursor.fetchone()
        reimbursement_request = ReimbursementRequest(*record)
        return reimbursement_request

    def get_all_reimbursement_requests(self) -> List[ReimbursementRequest]:
        sql = """select * from reimbursement_request"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        request_list = []
        for record in records:
            request_list.append(ReimbursementRequest(*record))
        return request_list

    def update_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        sql = """update reimbursement_request set e_id=%s, amount=%s, reason=%s, status=%s, m_id=%s, message=%s where 
        request_id =%s """
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement_request.employee_id, reimbursement_request.amount,
                             reimbursement_request.reason, reimbursement_request.status,
                       reimbursement_request.manager_id, reimbursement_request.message,
                       reimbursement_request.request_id))
        connection.commit()
        return reimbursement_request

    def delete_reimbursement_request(self, reimbursement_request_id: int) -> bool:
        sql = """delete from reimbursement_request where request_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_request_id])
        connection.commit()
        return True
