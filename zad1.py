# Zadanie 1
# Proszę zaimplementować klasę Point, która ma trzy właściwości i metodę. Wszystkie te atrybuty
# (właściwości i metody) powinny być publiczne. Po pierwsze należy zaimplementować konstruktor, aby
# zainicjować wartości trzech właściwości: x, y, z. Do drugie trzeba zaimplementować metodę
# square_sum() w klasie Point, która podniesie x, y, z do kwadratu i zwróci ich sumę


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def square_sum(self):
        return self.x**2 + self.y**2 + self.z**2