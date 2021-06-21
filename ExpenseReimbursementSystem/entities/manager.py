
class Manager:

    def __init__(self, manager_id: int, first_name: str, last_name: str, username: str, password: str):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def as_json_dict(self):
        return {
            "managerId": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "password": self.password
        }
