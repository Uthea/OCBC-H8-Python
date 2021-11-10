class Dog():
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Mom():
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color


class Children(Mom):
    def __init__(self, name, new_hair_color):
        super(Children, self).__init__(name, new_hair_color)
        # self.name = name
        # self.hair_color = new_hair_color


if __name__ == '__main__':
    miles = Dog('Miles', 4)
    budy = Dog('Miles', 9)

    # print(miles.age)
    # print(miles.name)
    # print(Dog.species)
    #
    # print(budy.age)
    # print(budy.name)

    # print(miles.description())
    # print(miles.speak('bark'))

    mom = Mom('ani', 'cokelat')
    print(f"{mom.name}'s hair color is {mom.hair_color}")
    first_daughther = Children('ita', 'ungu')
    print(f"{first_daughther.name}'s hair color is {first_daughther.hair_color}")
