class Test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a+self.b
        return c

t = Test(10,20)
add1 = t.add()
print(add1)



