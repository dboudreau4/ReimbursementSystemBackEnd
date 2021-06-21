

class ReimbursementRequest:

    def __init__(self, request_id: int, employee_id: int, amount: float, reason: str, status: str, manager_id: int, message: str):
        self.request_id = request_id
        self.employee_id = employee_id
        self.amount = amount
        self.reason = reason
        self.status = status
        self.manager_id = manager_id
        self.message = message

    def as_json_dict(self):
        return {
            "requestId": self.request_id,
            "employeeId": self.employee_id,
            "amount": self.amount,
            "reason": self.reason,
            "approved": self.status,
            "managerId": self.manager_id,
            "message": self.message
        }
