# Zadanie 4
# Proszę zaimplementować klasę Rectangle. Następnie proszę zaimplementować konstruktor, aby
# zainicjować wartości dwóch właściwości prywatnych: length i width. Należy także zaimplementować
# metodę area() w klasie Rectangle, która zwraca iloczyn długości i szerokości. Dodatkowo proszę
# zaimplementować metodę perimeter(), która służy do obliczania obwodu.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * self.__length + 2 * self.__width
