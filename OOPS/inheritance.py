

# creating parent class named as car

class Car:
    def __init__(self,car_type,engine_type,windos):
        self.car=car_type
        self.engine_type=engine_type
        self.windo=windos
        
    def drive(self):
        print(f"The person will drive the {self.car} this car...")
        
    
c=Car("Tyota","Tata",2)
print(c.drive())

# inheriting the car method
class Tesla(Car):
    def __init__(self,car_type,engine_type,windos,isSelfDriving):
        super().__init__(car_type,engine_type,windos)
        self.isSelfDriving=isSelfDriving
        
    def selfDrving(self):
        print(f"The person driving car is {self.car} is self Driving {self.isSelfDriving}")
        


t=Tesla("Tesla","Tesla Engine",4,"True")
print(t.selfDrving())
print(t.drive())



# creating multiple inheritance

class Animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print(f"Animal Speaks : {self.name}")
        
# second base class
class pet:
    def __init__(self,owner):
        self.owner=owner
        
    
    # Third class child inheriting animal and pet
class Dog(Animal,pet):
    def __init__(self,name,owner,Age):
        Animal.__init__(self,name)
        pet.__init__(self,owner)
        self.age=Age
        
    def sound(self):
        print(f"Anima {self.name} sound")
        
        
d=Dog("Dog","John",18)
print(d.sound())
print(d.speak())