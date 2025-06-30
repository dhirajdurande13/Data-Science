# Instance variable and method
class dog:
    # constructor
    # self keyword will use to avoid ambigutiy in formal and actual parameter or it work like this
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Constructor calling')
        # here self.name is like instance variable
        
dog1=dog("Chintu",18)
print(dog1.name)
print(dog1.age)


# creating class and defining methods inside that

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    # defining method
    def sound(self): #here we are passing self because ned to access this instance variables like name and age inside this 
        print(f"{self.name} Making sound")
        
c1=Cat("Billi",6)
c1.sound()



class Bank:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount Deposited {amount}! New Balance is {self.balance}")
        
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insuffiecent Balance")
        else:
            self.balance-=amount
            print(f"Amount withdraw {amount}! New Balance is {self.balance}")
            
    def get_balance(self):
        return self.balance
            
b1=Bank("Rishi",1000)
b1.deposit(200)
b1.withdraw(100)
print(b1.get_balance())