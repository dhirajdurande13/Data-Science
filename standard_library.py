import random
print(random.randint(1,10))
print(random.choice(['Apple','Banana','CHerry']))

import os
print(os.getcwd())


# import shutil
# shutil.copyfile('source.txt','destination.txt')


# Data serialization

import json
dict={
    "Name":"RIshi",
    "Age":21,
    "Marks":99,
    "Salary":"50K"
}

json_str=json.dumps(dict)
print(type(json_str))
print(json_str)
parsed_data=json.loads(json_str)
print(type(parsed_data))
print(parsed_data)


# creating csv

import csv

with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Age'])
    writer.writerow(['Rishi','18'])
    writer.writerow(['Mahesh','28'])
    
    
    
with open('example.csv',mode='r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)
        
        
from datetime import timedelta,datetime

now=datetime.now()
print(now)
oneDayback=now-timedelta(weeks=1)
print(oneDayback)



# import time
# print(time.time())
# time.sleep(2)
# print(time.time())

# reguler expression

import re
pattern=r'\d+'

text="there are lot of things in life and this are the numbers 123 456"

match=re.search(pattern,text)
print(match)


import math

print(math.sqrt(25))
print(math.sin(math.radians(90)))

from datetime import datetime
print(datetime.now())


from random import randint
print(randint(1,100))

from math import sqrt,pow
print(sqrt(16))
print(pow(3,2))



# Handaling non existing error

try:
    import non_existent
except ImportError as e:
    print(f"IMport error found {e}") 
    
    
import os
# os.mkdir('New Dir')
# print(os.listdir())
# os.rmdir('New Dir')


import sys
print(sys.version)
print(sys.argv)


print(math.gcd(48,6))
print(math.factorial(5))

from datetime import date
print(now+timedelta(days=100))
givendate=date(2025,1,1)
print(givendate)
print(givendate.strftime('%A'))



import random
lst=[]
for i in range(0,5):
    num=random.randint(1,50)
    lst.append(num)
    
print(lst)

lst=[1,2,3,4,5]
random.shuffle(lst)
print(lst)


# from mypackage import module1,module2
# print(module1.add_two(2,3))
# print(module2.mult_two(2,3))


# when we import this function from that module to __init__.py here we can directly use
from mypackage import add_two,mult_two
print(add_two(2,3))
print(mult_two(2,3))

# from mypackage.subpackage import module3
# print(module3.div_two(3,4))

# declaring in __init
from mypackage import div_two
print(div_two(3,4))



try:
    from mypackage import add_two
    # from mypackage import non_existent
    print(add_two(8,3))
except ImportError as e:
    print(f"Import Error-{e}")