import uuid
from datetime import datetime

class OrderService:

    def __init__(self):
        self.orders = []

    def create_order(self, data):
        order = {
            "id": str(uuid.uuid4()),
            "item": data["item"],
            "quantity": data["quantity"],
            "created_at": str(datetime.utcnow())
        }
        self.orders.append(order)
        return order

    def get_orders(self):
        return self.orders