class iphoneX:
    def camera(self):
        print("It has 2 cameras")

class iphone12(iphoneX):
    def camera(self):
        print("It has 3 Camera")
        super().camera()

x = iphoneX()
x.camera()

y = iphone12()
y.camera()

#In this MethodOverriding takes place where the methods in the 2 different classes have same method name as well as the parameter inside  it