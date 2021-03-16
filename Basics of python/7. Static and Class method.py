# Static and Class method
# Using self and cls and then nothing ...
class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """Bark n times"""
        for _ in range(n):
            print("Bark!")


# tim = Dog("Tim")
# jim = Dog("Jim")
# class methods
print(Dog.num_dogs())  # We did not ever created any instance and this works WOW

tim = Dog("Tim")
print(tim.num_dogs())

# static methods
Dog.bark(5)


# __________________________
class Math:
    @staticmethod
    def add(x, x2):
        return x + x2


print(Math.add(5, 2))

# We are not creating any object in this case directly calling add
