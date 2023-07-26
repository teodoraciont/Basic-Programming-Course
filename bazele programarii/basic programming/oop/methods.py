class Dog:
    normal_temperature = 25

    def __init__(self, name, kg, temperature):
        self.name = name
        self.kg = kg
        self.temperature = temperature

    def change_name(self, new_name):
        # metoda de instanta, acceseaza si modifica self.name din instanta
        self.name = new_name

    def is_temperature_normal(self):
        # metoda de instanta pentru ca acceseaza self.temperature.
        # Deoarece self are acces si la instanta, poate accesa si normal_temperature
        return self.temperature <= self.normal_temperature

    @classmethod
    def get_normal_temperature(cls):
        # metoda de clasa, pentru ca acceseaza un atribut al clasei, nu al instantei
        return cls.normal_temperature

    @staticmethod
    # metoda statica, nu acceseaza nimic din clasa, nu are nevoie de nimic din instanta
    def bark():
        print("Ham ham")


if __name__ == "__main__":
    zoe = Dog("Zoe", 15, 25.5)
    # aici avem nevoie de instanta zoe, pentru ca accesam o metoda a clasei Dog
    zoe.change_name("Zoe exploratarea")
    print("New name:", zoe.name)
    print("Is temperature normal for Zoe: ", zoe.is_temperature_normal())

    # nu ave, nevoie de o instanta a clasei Dog, putem folosi doar numele clasei
    print('normal temperature for dogs', Dog.get_normal_temperature())
    print('cum face catelul?')
    Dog.bark()
