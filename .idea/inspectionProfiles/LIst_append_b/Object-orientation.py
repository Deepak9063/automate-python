class FootBaller:
    def __init__(self,name,team,goal):
        self.name = name
        self.team = team
        self.goal = goal

    def shooting(self):
        print(self.name,"He is shooting")

    def playing(self):
        print(self.team,"He plays in barcelona")

    def running(self):
        print(self.goal,"He hits large number of goals")

    def display(self):
        print(self.name)
        print(self.team)
        print(self.goal)


def main():
    cr = FootBaller('messi','Balrcelona',32)#this is how the object creation is done
    print(cr.name)
    print(cr.team)
    print(cr.goal)
    cr.shooting()
    cr.playing()
    cr.running()

    cr2 = FootBaller('deep','India',88)
    print(cr2.display())
    cr2.shooting()
    cr2.playing()
    cr2.running()

if __name__ ==  '__main__':
    main()


