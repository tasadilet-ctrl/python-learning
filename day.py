class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"{self.name} is a pet and I don't know how to speak.")

class Dog(Pet):
    def speak(self):
        print(f"{self.name} says Woof!")
    
class Cat(Pet):
    def speak(self):
        print(f"{self.name} says Meow!")

Pet1 = Pet("Buddy", 5)
Dog1 = Dog("Rex", 3)
Cat1 = Cat("Whiskers", 2)

Pet1.speak()  # Output: Buddy is a pet and I don't know how to speak.
Dog1.speak()  # Output: Rex says Woof!
Cat1.speak()  # Output: Whiskers says Meow!