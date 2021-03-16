# Public and Private Classes
# In python there is no such thing but We can do this using program below
# We will use coding conventions
class _Private:
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("Hello!")

    def display(self):
        print("Hi!")

# We can use both the display but it is just a convention to use _ to denote that do not use this class or funtion

test = NotPrivate("Tanishka")
test.display()
test._display()