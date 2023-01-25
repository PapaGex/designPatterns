class Dog:
    """Dog Class"""


    def __init__(self,name):
        self._name = name

    def speak(self):
        return "Woof!"

def get_pet(pet="dog"):

    """The Factory Method"""

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

class Cat:


    def __init__(self):
        self._name = name

    def speak(self):
        return "Meow!"


