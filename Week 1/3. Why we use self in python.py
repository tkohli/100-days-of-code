# Why python has the self keyword everywhere
class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi! I am ",self.name,"and I am",str(self.age),"years old.")


tim = Dog("Tim", 5)
king = Dog("King", 8)
tim.speak()
king.speak()
print(tim.name)
print(king.age)
""" Output Hi! I am  Tim and I am 5 years old.
    Hi! I am  King and I am 8 years old.
    Tim
    8
    Here we can see that we can access both instances at the same time and for this python uses self keyword"""
