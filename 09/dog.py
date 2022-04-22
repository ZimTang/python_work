class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")


myDog = Dog('james', 37)

myDog.sit()
