class Coffee:
    def __init__(self, water_level, coffee_level, is_clean):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.is_clean = is_clean

    def make_coffee(self):
        print("Pls wait until the coffee is done...!")
        if not self._there_is_water():
            print("There is no water")
            return
        if not self._there_is_coffee():
            print("There is no water")
            return
        if not self.__is_machine_clean():
            print("Pls clean the machine")
            return
        print("Done, enjoy your coffee \U0001f600")

    def _there_is_water(self):
        return self.water_level > 10

    def _there_is_coffee(self):
        return self.water_level > 5

    def __is_machine_clean(self):
        return self.is_clean == True


class ExpresoCoffee(Coffee):

    def __init__(self, water_level, coffee_level):
        super().__init__(water_level, coffee_level, True)

    def _there_is_water(self):
        return self.water_level > 5

    def _there_is_coffee(self):
        return self.water_level > 2.5


if __name__ == "__main__":
    coffee = Coffee(30, 10, True)
    coffee.make_coffee()

    expreso = ExpresoCoffee(2.55, 2.5)
    expreso.make_coffee()
