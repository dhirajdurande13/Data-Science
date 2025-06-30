# Memory Management in python involves automatic garbage collection,reference counting,memory allocation,memory deallocation



# Refrence counting


import sys
a=[]
print(sys.getrefcount(a))


b=a
print(sys.getrefcount(b))


import gc
# garbage collector
gc.enable()
gc.disable()


print(gc.collect())

# get garbage collection stats
print(gc.get_stats())

# get unreachable garbage
print(gc.garbage)



class MyObject:
    def __init__(self,name):
        self.name=name
        print(f"{self.name} object is created")
        
    def __del__(self):
        print(f"{self.name} object is deleted")
        
# create circuler reference

obj1=MyObject("Object1")
obj2=MyObject("Object2")
obj1.ref=obj2
obj2.ref=obj1

del obj1 
del obj2

gc.collect()



# Genrators for memory efficency:Genrators allows us to genrate one item at a time

def genrate_numbers(n):
    for i in range(n):
        yield i
        #It allows function to pass value and pause a function
        
for num in genrate_numbers(10000):
    print(num)
    if num>10:
        break
    
    
    # trace malloc shows all memory profiling