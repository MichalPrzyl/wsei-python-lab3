# Zadane 2
# Proszę zaimplementować klasę — Student — która ma cztery właściwości i dwie metody. Wszystkie te
# atrybuty (właściwości i metody) powinny być publiczne. Należy zaimplementować konstruktor, aby
# zainicjować wartości czterech właściwości: name, phy, chem i bio. Następne proszę zaimplementować
# metodę – total_obtained() – w klasie Student, która oblicza sumę ocen ucznia. Za pomocą metody
# total_obtained() należy zaimplementować w klasie Student metodę percentage(), która oblicza
# procent ocen uczniów. Dodatkowym założeniem jest to, że suma ocen z każdego przedmiotu wynosi
# 100 - suma ocen z trzech przedmiotów wynosi 300.

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def total_obtained(self):
        return self.name + self.phy + self.chem + self.bio

    def percentage(self):
        # totalnie nie wiem czy o to chodzi. Dziwnie skonstruowane zdanie w
        # zadaniu
        return self.total_obtained() / 400
