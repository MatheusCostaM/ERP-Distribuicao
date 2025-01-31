class User:
    def __init__(self, user_id, user_name, user_type):
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def get(self) -> dict:
        return {
            "id": self.user_id,
            "name": self.user_name,
            "type": self.user_type
        }

    def set_name(self, name: str):
        self.user_name = name

    def set_type(self, type: str):
        self.user_type = type
