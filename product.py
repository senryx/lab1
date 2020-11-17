class Product:
    def __init__(self, price, delivery, description):
        self.__price = price
        self.__delivery = delivery
        self.__description = description

    def set_price(self, price):
        self.__price = price

    def set_delivery(self, delivery):
        self.__delivery = delivery

    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price

    def get_delivery(self):
        return self.__delivery

    def get_description(self):
        return self.__description

    def get_product(self):
        print(
            f"price: {self.__price}\ndelivery: {self.__delivery}\namount: {self.__description}"
        )
