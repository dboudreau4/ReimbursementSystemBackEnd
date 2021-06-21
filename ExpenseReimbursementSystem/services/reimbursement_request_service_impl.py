from daos.reimbursement_request_dao import ReimbursementRequestDAO
from entities.reimbursement_request import ReimbursementRequest
from services.reimbursement_request_service import ReimbursementRequestService


class ReimbursementRequestServiceImpl(ReimbursementRequestService):

    def __init__(self, reimbursement_request_dao: ReimbursementRequestDAO):
        self.reimbursement_request_dao = reimbursement_request_dao

    def add_reimbursement_request(self, reimbursement_request: ReimbursementRequest):
        return self.reimbursement_request_dao.create_reimbursement_request(reimbursement_request)

    def retrieve_all_reimbursement_requests(self):
        return self.reimbursement_request_dao.get_all_reimbursement_requests()

    def retrieve_reimbursement_request_by_id(self, reimbursement_request_id: int):
        return self.reimbursement_request_dao.get_reimbursement_request(reimbursement_request_id)

    def update_reimbursement_request(self, reimbursement_request: ReimbursementRequest):
        return self.reimbursement_request_dao.update_reimbursement_request(reimbursement_request)

    def remove_reimbursement_request(self, reimbursement_request_id: int):
        return self.reimbursement_request_dao.delete_reimbursement_request(reimbursement_request_id)