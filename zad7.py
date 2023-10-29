# Zadanie 7
# Proszę przygotować klasę nadrzędną o nazwie Animal. Wewnątrz niej proszę zdefiniować: name,
# sound, __init__(), animal_details(). Ostatnia metoda ma za zadanie wyświetlić imię zwierzęcia dźwięk
# jaki wydaje. Następnie proszę przygotować dwie klasy pochodne: Dog oraz Sheep. Pierwsza z nich
# powinna posiadać następujące cechy: własność family, konstruktor, który wywołuje konstruktor klasy
# nadrzędnej za pomocą super(). Posiada także nadpisaną metodę o nazwie animal_details(). Klasa
# Sheep, posiada własność color. Wywołuje konstruktor klasy nadrzędnej za pomocą super(). Posiada
# także nadpisaną metodę o nazwie animal_details().

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def animal_details(self):
        print(f"name: {self.name}")
        print(f"sound: {self.sound}")

    def __str__(self):
        return self.name


class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def animal_details(self):
        print(f"family: {self.family}")
        super().animal_details()


class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def animal_details(self):
        print(f"color: {self.color}")
        super().animal_details()
