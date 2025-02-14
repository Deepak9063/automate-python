class Aplha:
    def fun1(self):
        print("Came from alpha function")

class Beta(Aplha):
    def fun2(self):
        print("Came from beta class")

class Gamma(Beta):
    pass

g = Gamma()
g.fun1()
g.fun2()