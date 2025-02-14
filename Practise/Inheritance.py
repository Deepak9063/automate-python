class Animal:
    def herbivorus(self):
        print("It eats grass")

class Reptiles(Animal):
    def snake(self):
        print("Snake will bite it is very poisonous")

        super().herbivorus()

rep = Reptiles()
rep.snake()
