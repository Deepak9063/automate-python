class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length*self.breadth)

class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height = h
        super().__init__(l,b)

    def volume(self):
        return self.length*self.breadth*self.height

c = Rectangle(10,20)
print(c.area())
print(c.perimeter())

r = Cuboid(10,20,30)
print(r.volume())

