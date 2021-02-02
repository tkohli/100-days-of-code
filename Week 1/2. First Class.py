# Writing our first class. Note- This is actually my first class program
class Dog(object):
    def __init__(self):
        print("Hey I am just making an instance of this class Why is this line printing")

    def speak(self):
        print("Bark!!!")

tim = Dog()

""" As we can see here that we directly get output Hey I am just making an instance of this 
    class Why is this line printing 
    This is what init function do, it is a type of Constructor which is automatically called 
    everytime """

tim.speak()
"""We get output as Bark
"""
