
class Animal:
    def speak(self):
        return "Animal Sound"
    
class Cat(Animal):
    def speak(self):
        return "Cat Sound"
    
class Dog(Animal):
    def speak(self):
        return "Dog sound"
# Above is the function overriding

def animal_speak(animal):
    print(animal.speak())

d=Dog()   
C=Cat()
print(d.speak())
print(C.speak())
animal=Animal()
animal_speak(animal)



# creating Area example

class Shape:
    def area(self):
        return "The area of figure is"
    
class rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
        
    def area(self):
        return self.height*self.width
    
class circle():
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14 * self.radius *self.radius
    
def print_area(shape):
    print(f"Area is {shape.area()}")
    
c=circle(7)
r=rectangle(3,4)
print(print_area(r))
print(print_area(c))

print(dir(c))  #To show all the atributes of the circle