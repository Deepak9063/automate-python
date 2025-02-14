class Dog:
    def talk(self):
        print("Dog is talking")

    def walk(self):
        print("Dog is walking")

class Cat:
    def talk(self):
        print("Cat is talking")

    def walk(self):
        print("Cat is walking")

def pet(a):
    a.talk()
    a.walk()

d = Dog()
pet(d)

c = Cat()
pet(c)





