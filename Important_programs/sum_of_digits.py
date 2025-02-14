#Inheritance

class Car:
    def hatchback(self):
        print("They are very esy to park")

    def sedan(self):
        print("They are difficult to park")

class Suv(Car):
    def suv(self):
        print("They are very huge car segment")
    super().hatchback()
    super().sedan()

suv_obj = Suv()
suv_obj.suv()
