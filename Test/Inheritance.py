class Animal:
    def dog(self):
        print("BowBow")

    def cat(self):
        print("Meow")

class Herbivorous(Animal):
    def buffalow(self):
        print("It eats grass")
        super().dog()
        super().cat()
h = Herbivorous()
h.buffalow()


class Animal:
    def dog(self):
        print("Dog is barking")

    def cat(self):
        print("Cat is very cute")

class Herbivorous(Animal):
    def snake(self):
        print("Snake bites")

        super().dog()
        super().cat()

herb = Herbivorous()
herb.snake()


