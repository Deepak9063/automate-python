# from abc import ABC
# class Shape(ABC):
#     def area(self,l,b):
#         pass
#
#     def perimeter(self,l,b):
#         p = 2*l*b
#         print(p)
#
# class Cube(Shape):
#     def area(self,l,b):
#         c = l*b
#         print(c)
#
#
# s = Shape()
#
# c = Cube()
# c.area(2,5)
# c.perimeter(5,6)

class Shape:
    def area(self,l,b):
        pass

    def perimeter(self,l,b):
        p = 2*l*b
        return p

class Cube(Shape):
    def area(self,l,b):
        a = l*b
        return a
s = Shape()
area = s.area(2,4)
print(area)
perimeter = s.perimeter(5,6)
print(perimeter)
c = Cube()
area2 = c.area(8,9)
print(area2)



