# lambda argument:expression


addition =lambda a,b: a+b
print(addition(2,3))


even=lambda num:num%2==0
print(even(24))

add=lambda x,y,z:x+y+z
print(add(2,3,4))

sqr=lambda x:x**2
print(sqr(2))

number=[1,2,3,4,5]

sqr_num=list(map(lambda x:x**2,number))
print(sqr_num)

number1=[1,2,3,4,5]
number2=[1,2,3,4,5]
multiplay=list(map(lambda x,y:x*y,number1,number2))
print(multiplay)


lst=["1","2","3","4","5"]
print(list(map(lambda x:int(x),lst)))


fruits=["apple","Banana","Grapse"]

print(list(map(lambda ele:ele.upper(),fruits)))



people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33}
]

person_name=list(map(lambda ele:ele['name'],people))
print(person_name)


# filter function construct an iterator for element which have condition true

lst=[1,2,3,4,5,6,7,8,9,10,11,12]

def even(x):
    if x%2==0:
        return True
    
print(list(filter(even,lst)))

greater_5=list(filter(lambda x:x>5,lst))
print(greater_5)


mult_cond=list(filter(lambda x:x>5 and x%2==0 ,lst))
print(mult_cond)


people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]


age_great_25=list(filter(lambda ele:ele['age']>25 ,people))
print(age_great_25)