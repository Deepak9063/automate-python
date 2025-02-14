class Animal:
    def dog(self):
        print("Dog will bark")

class Reptiles(Animal):
    def snake(self):
        print("Snake will bite")

        super().dog()

r = Reptiles()
r.snake()
