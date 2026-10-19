from enum import Enum

class OrderStatus(Enum):
        PENDING = 1
        PROCESSING = 2
        SHIPPED = 3
        DELIVERED = 4
        CANCELED = 5

class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = OrderStatus.PENDING
    
    def update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.status = new_status
            print(f'Order {self.order_id} updated to {self.status.name}')
        else:
            print('Invalid')
    
    def display(self):
        print(f'Order Id: {self.order_id}')
        print(f'Customer: {self.customer_name}')
        print(f'Status: {self.status}')



order1 = Order(101, "Peter")   
order1.display()
order1.update_status(OrderStatus.PROCESSING)
order1.update_status(OrderStatus.SHIPPED)
order1.update_status(OrderStatus.DELIVERED)
order1.update_status(OrderStatus.CANCELED)