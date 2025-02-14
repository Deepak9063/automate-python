class AccountHolder:
    def __init__(self):
        self.__bal = 10000  #Where __bal helps in dataMangling

    def get_bal(self):
        return self.__bal

    def set_bal(self):
        if amt>0:
            self.__bal = amt

        else:
            print("Amount entered is not valid")

ac = AccountHolder()
print(ac.__dict__)
#print(ac.__bal)   #This is invalid where it uses dataMangling Its syntax is _className__VariableName
print(ac._AccountHolder__bal)                                                                     #   _AccountHolder__bal the it givesv the output

