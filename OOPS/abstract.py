# Polymorphism with abstract class:
# ABC is known as abstract class


from abc import ABC,abstractmethod

# Define abstract class

# diffrence between the normal class and abstract class is here we are inheriting ABC which is abstract base class
class vehicle(ABC):
    # this is abstract method which is always empty means only declaration is here defination is in derived class
    @abstractmethod
    def start_engine(self):
        pass
    
    
class car(vehicle):
    def start_engine(self):
        return "Car engine Started"
    
# derived class 2
class motor_cycle(vehicle):
    def start_engine(self):
        return "Motor Cycle Engine"
    
c=car()
m=motor_cycle()

print(c.start_engine())
print(m.start_engine())



# By default all declared variables and methods are public

class Human:
    def __init__(self,name,age,sex):
        self._name=name  #single underscore is protected variable :protected is we can access only in base class and child class other we canrt use 
        self.__age=age  #If we use double under score then it will automatically be an private 
        self.sex=sex #this is Public
    # Here in this example we are only able to see public variables not private
h=Human("Rishi",22,"Male")    
# print(dir(h))



# Encapsulation where we are using getter and setter methods
# Accessing private variables we use getter and setter methods
class Person:
    def __init__(self,age,name):
        self.__age=age
        self.__name=name
        
    def set_name(self,name):
        self.__name=name
        
        # Age setter 
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age Can't be -ve")
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name        
        
        
per=Person(21,"Rishi")
print(per.get_age())
print(per.get_name())



# creating abstraction 
from abc import ABC,abstractmethod
class Vehicle(ABC):
    def drive(self):
        print("Vehicle used for driving")
        
    @abstractmethod
    def start_engine(self):
        pass
    
class car(Vehicle):
    def start_engine(self):
        print("Car engine started")
        
def operate(veh):
    veh.start_engine()        
    
    
# we cant call abstract class directly need to create car object
veh=car()
operate(veh)


# Overriding default str function
# Magic function
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name},{self.age} Person"
    def __repr__(self):
        return f"{self.name},{self.age} Person With official string representation"
    
p=Person("Rishi",22)
print(p) #it is retuning because we override this default str function 
print(repr(p))  



# Mathematical operation for vector with operator overloading

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    
v1=Vector(2,3)
v2=Vector(4,6)

print(v1+v2)
print(v1-v2)
print(v1*v2)



class complex_number:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        
    def __add__(self,other):
        return complex_number(self.real+other.real,self.imag+other.imag)
    def __str__(self):
        return f"COmplex_number({self.real},{self.imag}i)"
    
c1=complex_number(3,4)
c2=complex_number(4,5)

print(c1+c2)