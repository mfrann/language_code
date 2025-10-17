

class Person:

    def __init__(self):
        self.name=input("Add user: ")
        self.age=input("Add age: ")
    
    def toPrint(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Cityzen(Person):
    def __init__(self):
        super().__init__()
        self.deposit=float(input("Add deposit: "))
    def toPrint(self):
        super().toPrint()
        print("Deposit: ", self.deposit)
    def tax(self):
        if self.deposit > 4000:
            print(f'{self.name} must pay taxes')
        else:
            print(f'{self.name} must not pay taxes')

citizen1 = Cityzen()
citizen1.toPrint()
citizen1.tax()


'''
MANUEL -> PAGA 
FAYLE -> NO PAGA
LESLY -> PAGA
MARIO -> NO PAGA

'''