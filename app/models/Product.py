class Product:
    def __init__(self, product_id, product_name, product_price, product_type):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_type = product_type

    def get(self) -> dict:
        return {
            "id": self.product_id,
            "name": self.product_name,
            "price": self.product_price,
            "type": self.product_type
        }

    def set_name(self, name: str):
        self.product_name = name

    def set_price(self, price: float):
        self.product_price = price

    def set_type(self, type: str):
        self.product_type = type
