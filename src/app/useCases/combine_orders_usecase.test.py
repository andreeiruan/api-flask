from .combine_orders_usecase import Orders

orders = [70, 30, 10]
n_max = 100
expected_orders = 2

how_many = Orders().combine_orders(orders, n_max)

assert how_many == expected_orders

orders = [70, 30, 10, 40, 80, 50, 70, 45, 30, 90]
n_max = 100
expected_orders = 6

how_many = Orders().combine_orders(orders, n_max)

assert how_many == expected_orders
