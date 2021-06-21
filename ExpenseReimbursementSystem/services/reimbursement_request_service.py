from abc import ABC, abstractmethod

from entities.reimbursement_request import ReimbursementRequest


class ReimbursementRequestService(ABC):

    @abstractmethod
    def add_reimbursement_request(self, reimbursement_request: ReimbursementRequest):
        pass

    @abstractmethod
    def retrieve_all_reimbursement_requests(self):
        pass

    @abstractmethod
    def retrieve_reimbursement_request_by_id(self, reimbursement_request_id: int):
        pass

    @abstractmethod
    def update_reimbursement_request(self, reimbursement_request: ReimbursementRequest):
        pass

    @abstractmethod
    def remove_reimbursement_request(self, reimbursement_request_id: int):
        pass
