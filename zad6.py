# Zadanie 6
# Proszę zaimplementować podstawową strukturę klasy nadrzędnej Account i klasy podrzędnej
# SavingsAccount. Proszę zaimplementować właściwości jako zmienne instancji i ustawić je na None lub
# 0. Klasa Account ma następujące właściwości: title, balance. SavingsAccount posiada następujące
# właściwości – interest_rate. W klasie Account trzeba zaimplementować metodę get_balance(), która
# zwraca saldo. W klasie Account proszę zaimplementować metodę deposit(amount), która dodaje
# kwotę do salda (kwota musi być nieujemna, należy ustawić odpowiednie zabezpieczenie). W klasie
# Account proszę zaimplementować metodę withdraw(amount), która odejmuje kwotę od salda (kwota
# musi być nieujemna, należy ustawić odpowiednie zabezpieczenie). W klasie SavingsAccount proszę
# zaimplementować metodę interest_amount(), która zwraca kwotę odsetek bieżącego salda według
# wzoru: interest_rate ∗ balance
# 100 .

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def __str__(self):
        return self.title

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("You cannot add negative value to balance")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("You cannot add negative value to balance")
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(title, balance)

    def interest_amount(self):
        return (self.interest_rate * self.balance) / 100
