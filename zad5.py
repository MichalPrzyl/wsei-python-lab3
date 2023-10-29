# Zadanie 5
# Proszę zaimplementować klasę Student. Proszę zaimplementować następujące właściwości jako
# prywatne: name, roll_number. Następnie należy zaimplementować następujące metody, aby uzyskać
# i ustawić powyższe właściwości prywatne: getName(), setName(), getRollNumber(), setRollNumber()


class Student:
    def __init__(self):
        self.__name = ''
        self.__roll_number = ''

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_roll_number(self):
        return self.__roll_number

    def set_roll_number(self, value):
        self.__roll_number = value
