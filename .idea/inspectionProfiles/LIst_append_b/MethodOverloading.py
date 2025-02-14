class Animal():
    def make_sound(self):
        print("Animals make sound")

class Dog(Animal):
    def make_sound(self):
        print("BowBow")

class Cat(Dog):
    def make_sound(self):
        print("Meow")


animals = [Dog(),Cat()]

for i in animals:
    print(i.make_sound())