from daos.reimbursement_request_dao import ReimbursementRequestDAO
from daos.reimbursement_request_dao_postgres import ReimbursementRequestDAOPostgres
from entities.reimbursement_request import ReimbursementRequest

reimbursement_request_dao: ReimbursementRequestDAO = ReimbursementRequestDAOPostgres()

# request_id: int, employee_id: int, reason: str, status: bool, manager_id: int, message: str
test_request = ReimbursementRequest(0, 3, 500, "Office supplies", "pending", 1, "")


def test_create_request():
    reimbursement_request_dao.create_reimbursement_request(test_request)
    assert test_request.request_id != 0


def test_get_request():
    request = reimbursement_request_dao.get_reimbursement_request(test_request.request_id)
    assert test_request.request_id == request.request_id


def test_get_all_requests():
    request1 = ReimbursementRequest(0, 3, 100, "Office supplies", "pending", 1, "")
    request2 = ReimbursementRequest(0, 3, 200, "Office supplies", "pending", 1, "")
    request3 = ReimbursementRequest(0, 3, 300, "Office supplies", "pending", 1, "")
    reimbursement_request_dao.create_reimbursement_request(request1)
    reimbursement_request_dao.create_reimbursement_request(request2)
    reimbursement_request_dao.create_reimbursement_request(request3)
    requests = reimbursement_request_dao.get_all_reimbursement_requests()
    assert len(requests) >= 3


def test_update_request():
    test_request.message = "Amount too much"
    updated_request = reimbursement_request_dao.update_reimbursement_request(test_request)
    assert updated_request.message == test_request.message


def test_delete_request():
    result = reimbursement_request_dao.delete_reimbursement_request(test_request.request_id)
    assert result
