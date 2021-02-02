# Inheritance
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi! I am ", self.name, "and I am", str(self.age), "years old.")


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


tim = Cat('Tim', 5, 'Blue')
tim.speak()
""" We used Dog as our Parent class and inherited it into Cat then called speak function that is
    defined in Dog and called it using Cat."""
