class Sales:
    def __init__(self, sales_id: int, sales_quantity: int, sales_date: str, user_id: int, product_id: int, client_id: int):
        self.sales_id = sales_id
        self.sales_quantity = sales_quantity
        self.sales_date = sales_date
        self.user_id = user_id
        self.product_id = product_id
        self.client_id = client_id

    def get(self) -> dict:
        return {
            "id": self.sales_id,
            "quantity": self.sales_quantity,
            "date": self.sales_date,
            "user": self.user_id,
            "product": self.product_id,
            "client": self.client_id
        }

    def set_quantity(self, quantity: int):
        self.sales_quantity = quantity

    def set_date(self, date: str):
        self.sales_date = date

    def set_user(self, user: int):
        self.user_id = user

    def set_product(self, product: int):
        self.product_id = product

    def set_client(self, client: int):
        self.client_id = client
