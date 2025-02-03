class Purchase:
    def __init__(self, purchase_id: int, purchase_quantity: int, purchase_date: str, purchase_value: float, product_id: int):
        self.purchase_id = purchase_id
        self.purchase_quantity = purchase_quantity
        self.purchase_date = purchase_date
        self.purchase_value = purchase_value
        self.product_id = product_id
        self.obj = 'purchase'

    def get(self) -> dict:
        return {
            "id": self.purchase_id,
            "quantity": self.purchase_quantity,
            "date": self.purchase_date,
            "value": self.purchase_value,
            "product": self.product_id
        }

    def set_quantity(self, quantity: int):
        self.purchase_quantity = quantity

    def set_date(self, date: str):
        self.purchase_date = date

    def set_value(self, value: float):
        self.purchase_value = value

    def set_product(self, product_id: int):
        self.product_id = product_id
