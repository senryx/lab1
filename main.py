from client import Client
from product import Product
from orders import Orders


def main():
    client1 = Client('max', 'street', 564654)
    product1 = Product(100, 'two days', 'description')
    order1 = Orders(client1, product1, 5, '20.11.2005')
    order1.print_order()
    order1.set_amount(10)
    print("-" * 80)
    order1.print_order()
    client1.set_name('igor')
    product1.set_price(200)
    print("-" * 80)
    order1.print_order()


if __name__ == "__main__":
    main()
