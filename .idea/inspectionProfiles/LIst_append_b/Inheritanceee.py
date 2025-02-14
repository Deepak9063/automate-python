class Square:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

class Rectangle(Square):
    def __init__(self,height,length,breadth):
        self.height = height

        super().__init__(length,breadth)


    def volume(self):
        return self.length*self.breadth*self.height

s = Square(20,30)
r = Rectangle(40,50,60)

print(s.area())
print(r.volume())



