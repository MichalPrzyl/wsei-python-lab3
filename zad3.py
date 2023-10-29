# Zadanie 3
# Proszę napisać klasę o nazwie Calculator. Należy zaimplementować konstruktor, aby zainicjować
# wartości num1 i num2. Następnie proszę zaimplementować następujące metody:
# add() to metoda, która zwraca sumę liczb num1 i num2.
# subtract() to metoda, która zwraca odejmowanie liczby num1 od liczby num2.
# multiple() to metoda, która zwraca iloczyn liczb num1 i num2.
# div() to metoda, która zwraca dzielenie liczby num1 przez num2 (należy sprawdzić czy num2 jest różne
# od 0, jeśli nie jest należy wypisać odpowiedni komunikat. *W tym przypadku można także skorzystać z
# bloku try/exception).
# mod() to metoda, która zwraca modulo liczby num1 przez num2 (należy sprawdzić czy num2 jest różne
# od 0, jeśli nie jest należy wypisać odpowiedni komunikat. *W tym przypadku można także skorzystać z
# bloku try/exception).
# pow() to metoda, która podniesie num1 do potęgi num2 (należy pamiętać, że zero do potęgi zerowej
# nie jest jednoznaczny – w takim sytuacji należy wypisać odpowiedni komunikat. *W tym przypadku
# można także skorzystać z bloku try/exception).


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiple(self):
        return self.num2 * self.num1

    def div(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print("Num2 is 0. We can't divide")
            return 0
