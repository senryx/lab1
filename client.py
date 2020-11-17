class Client:
    def __init__(self, name, address, phonenumber):
        self.__name = name
        self.__address = address
        self.__phonenumber = phonenumber

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phonenumber(self):
        return self.__phonenumber

    def get_client(self):
        print(
            f"name: {self.__name}\naddress: {self.__address}\nphonenumber: {self.__phonenumber}"
        )
