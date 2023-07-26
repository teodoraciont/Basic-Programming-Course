class Car:
    # clasa generala, care tine toate atributele generale a clasei
    def __init__(self, window_nr, wheel_nr, km, color, name):
        self.window_nr = window_nr
        self.wheel_nr = wheel_nr
        self.km = km
        self.color = color
        self.name = name

    def car_specifications(self):
        return ("Car specifications: "
                "name: {},"
                " color: {},"
                " km: {},"
                " number of wheels: {}"
                " number of windows: {}"
                ).format(self.name, self.color, self.km, self.wheel_nr, self.window_nr)


class Van(Car):
    # clasa Van mosteneste clasa Car
    def __init__(self, window_nr, wheel_nr, km, color, name, type):
        # apelam constructorul clasei de baza
        super().__init__(window_nr, wheel_nr, km, color, name)

        # adaugam un nou parametru, care nu exista in Car
        self.van_type = type

    def van_specifications(self):
        basic_specifications = self.car_specifications()
        return "This is a van. Here's some info: " \
               "{} van type: {}".format(
                basic_specifications, self.van_type
                )


if __name__ == "__main__":
    basic_car = Car(4, 4, 2000, "red", "Mercedes")
    print(basic_car.car_specifications())
    van = Van(4, 8, 122000, "red", "Ford", "Step van")
    print(van.van_specifications())
