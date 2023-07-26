# class definition
class Dog:
    # constructor = se apeleaza prima data cand o instanta este creeata
    def __init__(self, dog_name, dog_type, dog_kg):
        # atributs: name, type, kg
        self.name = dog_name
        self.type = dog_type
        self.kg = dog_kg

    # method
    def get_dog_sound(self):
        print("HAM")

    # method
    def get_dog_info(self):
        print("Dog info: name {}, type: {}, kg:{}".format(self.name, self.type, self.kg))


if __name__ == "__main__":
    # class instances
    # instanta a clasei Dog
    zoe = Dog("Zoe", "-", 15) #se creeaza clasa Dog adica se apeleaza constructorul
    zoe.get_dog_info()
    zoe.get_dog_sound()
    # instanta a clasei Dog
    leia = Dog("Leia", "ciobanesc german", 20)
    leia.get_dog_info()
    leia.get_dog_sound()
