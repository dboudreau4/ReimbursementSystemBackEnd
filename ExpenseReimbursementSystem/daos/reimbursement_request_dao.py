from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement_request import ReimbursementRequest


class ReimbursementRequestDAO(ABC):

    @abstractmethod
    def create_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        pass

    @abstractmethod
    def get_reimbursement_request(self, reimbursement_request_id: int) -> ReimbursementRequest:
        pass

    @abstractmethod
    def get_all_reimbursement_requests(self) -> List[ReimbursementRequest]:
        pass

    @abstractmethod
    def update_reimbursement_request(self, reimbursement_request: ReimbursementRequest) -> ReimbursementRequest:
        pass

    @abstractmethod
    def delete_reimbursement_request(self, reimbursement_request_id: int) -> bool:
        pass
