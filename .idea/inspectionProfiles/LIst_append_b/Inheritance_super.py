class Customer:
    def __init__(self,name,ph_no,email):
        self.name = name
        self.ph_no = ph_no
        self.emai = email

class PlatinumCustomer(Customer):
    def __init__(self,name,ph_no,email,plat_id):
        super().__init__(name, ph_no, email)   #Here constructor chaining happens
        self.plat_id = plat_id

    def display(self):
        print(self.name)
        print(self.plat_id)
        print(self.ph_no)
        print(self.name)

def main():
    p = PlatinumCustomer('Deepak',7892119045,'deepakshetty1253@gmail.com',22)

    p.display()

if __name__ == '__main__':
    main()