def Animal(pet):
    pet.talk()
    pet.walk()

    if(hasattr(pet,'walk')):  #This helps when method is not present by using if condition we can use
        pet.walk()

class Cat:
    def talk(self):
        print("Cat is making sound")

    def walk(self):
        print("Cat is walking")

class Dog:
    def talk(self):
        print("Dog is barking")

  #  def walk(self):
       # print("Dog is walking")

c = Cat()
d = Dog()

d.talk()
#d.walk()

c.talk()
c.walk()

