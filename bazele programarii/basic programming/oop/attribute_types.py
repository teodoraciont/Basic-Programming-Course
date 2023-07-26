class Dog:
    # atribut de clasa - constant
    normal_temperature = 25

    def __init__(self, dog_name, dog_type, dog_kg):
        # atribute de instante - specifice pt fiecare obiect
        self.name = dog_name
        self.type = dog_type
        self.kg = dog_kg


if __name__ == "__main__":
    zoe = Dog("Zoe", "-", 15)
    print(zoe.normal_temperature, "zoe tempeture")
    leia = Dog("Leia", "ciobanesc german", 20)
    print(leia.normal_temperature, "leia tempeture")
