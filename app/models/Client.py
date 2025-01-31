class Client:
    def __init__(self, client_id, client_name):
        self.client_id = client_id
        self.client_name = client_name

    def get(self) -> dict:
        return {
            "id": self.client_id,
            "name": self.client_name,

        }

    def set_name(self, name: str):
        self.client_name = name
