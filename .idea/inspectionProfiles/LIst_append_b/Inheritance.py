class Alpha:
    def fun(self):
        print("This is alpha class fun()")

class Beta(Alpha):   #Where inheritance takes place here
    pass

b = Beta()
b.fun()