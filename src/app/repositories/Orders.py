class OrderRepository:
    def get_daily_orders(self):
        return [70, 30, 10, 40, 80, 50, 70, 45, 30, 90]

    def get_maximum_travel_value(self):
        return 100


orders_repository_singleton = OrderRepository()
