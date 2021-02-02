# Overloading
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark!!!")


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow!!!")


tim = Cat('Tim', 5, 'Blue')
tim.speak()
""" Output Meow!!!
    We used Dog as our Parent class and inherited it into Cat then called speak function that is
    overloaded as we used same name for both functions"""
