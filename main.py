class Person:
    first_name: object
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.show_info_another()

    def show_info_another(self) -> None:
        print("created")


def main():
    p1 = Person("Michał", "Przyłucki")
    print(p1)

if __name__ == "__main__":
    main()