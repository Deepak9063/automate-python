class BMW:
    def __init__(self,name ,cc,color):
        self.name = name
        self.cc = cc
        self.color = color

    @classmethod
    def x1(cls):
        return cls('x1',2900,'blue')

    @classmethod
    def I8(cls):
        return cls('I8',2400,'black')

    @classmethod
    def Series5(cls):
        return cls('Series5',4000,'Red')

    def display(self):
        print(self.name)
        print(self.color)
        print(self.cc)

def main():
    c1 = BMW.x1()
    c2 = BMW.I8()

if __name__ == '__main__':
    main()

