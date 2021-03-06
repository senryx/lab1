class Orders:
    def __init__(self, client, product, amount, date):
        self.__client = client
        self.__product = product
        self.__amount = amount
        self.__date = date

    def set_amount(self, amount):
        self.__amount = amount

    def set_date(self, date):
        self.__date = date

    def get_client_name(self):
        return self.__client.get_name()

    def get_product(self):
        return self.__product

    def get_order_price(self):
        return self.__amount * self.__product.get_price()

    def get_amount(self):
        return self.__amount

    def get_date(self):
        return self.__date

    def print_order(self):
        self.__product.get_product()
        self.__client.get_client()
        print(
            f"orderprice: {self.get_order_price()}\namount: {self.get_amount()}\ndate: {self.get_date()}"
        )
