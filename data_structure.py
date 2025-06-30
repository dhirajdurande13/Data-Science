lst=["RIshi","12",13,14,8.9]

print(type(lst))
print(lst)
print(lst[0])
print(lst[2])
print(lst[-1])

lst[1]="Director"
print(lst)
print(lst[1:])
lst.insert(2,"13")
print(lst)
lst.reverse()
print(lst)
print(lst[::-1])

# for ele in lst:
#     print(ele)

for idx,ele in enumerate(lst):
    print(idx,ele)
    
 
lst=[]    
for x in range(10):
    lst.append(x**2)
    
print(lst)

# Nested list comphresession

pair=[(x,y) for x in range(1,3) for y in range(5,8)]
print(pair)

print([x**2 for x in range(10)])

even=[x for x in range(10) if x%2==0]
print(even)


lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[(x,y) for x in lst1  for y in lst2]
print(pair)

lst1=["rishi","mahesh","abcd","efgh"]

lenList=[len(ele) for  ele in lst1]
print(lenList)



lst=["pay bills","Go","run"]

lst.append("Play")
print(lst)
lst.remove("run")
print(lst)
if "Go" in lst:
    print("Go Fast")
    
for task in lst:
    print(f"-{task}")
    
    
grades=[80,90,75,77]

print(f"Average is: {sum(grades)/len(grades)}")
print(f"Higest is: {max(grades)}")
print(f"Lowest is: {min(grades)}")

lst=["Apple","Banana","Mango"]
fruit="Banana"
if fruit in lst:
    print(f"Fruit is in {fruit}")
else:
     print(f"Fruit is Not in {fruit}")
     
     
feedback = ["Great service!", "Very satisfied", "Could be better", "Excellent experience"]

# positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())


positive_feedback_count=sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"Positive Feedback Count: {positive_feedback_count}")


lst=list()
tpl=tuple()
print(type(lst))
print(type(tpl))


lst=([1,2,3,4],["rishi","mahesh",45],[1.3,2,4])
print(lst[0][2:])

# nested tuple
lst=((1,2,3),("Rishi","MAhesh","Ganesh"))
print(lst[0])


# itertaing
for sub_tupple in lst:
    for ele in sub_tupple:
        print(ele,end=" ");
    print()
    
    
st={1,2,2,3,4,4}
# print(st)
# st=[{2,2,3,4,4},{5,5,6,7,7}]
# st=set([1,2,3,4,5,4,5])
st.add(15)
print(st)
st.remove(2)
print(st)
print(3 in st)
print(16 in st)


st1={1,1,2,3,4}
st2={5,5,6,6,7}
print(st1.union(st2))
print(st1.difference(st2))
print(st1.symmetric_difference(st2))

print(st2.issuperset(st1))
lst=[1,2,3,4,5]

print(set(lst))


text="In this tutorial we are discussing about sets"
word=text.split()
for ele in word:
    print(ele,end=" ")
    
st=set(word)
print(st)

dict={"name":"Rishi","Age":34,"Dream":"Money"}
print(dict.get("name"))
print(dict.get("wife","sita"))
dict["wife"]="sita"
print(dict)

print(dict.keys())
print(dict.values())
print(dict.copy())

for key,value in dict.items():
    print(f"keys:{key}->value:{value}")
    
    
students={
    "student1":{"name":"Rishi","age":15},
    "student2":{"name":"Mahesh","age":18}
}
print(students["student1"])


for student_id,student_info in students.items():
    print(student_id,student_info)
    for key,value in student_info.items():
        print(f"{key}->{value}")
        
        
        
dict={x:x**2 for x in range(10) if x%2==0}
print(dict)


numbers=[1,2,2,3,3,3,4,4,4,4,5,5]
frequency={}

for ele in numbers:
    if ele in frequency:
        frequency[ele]=frequency[ele]+1
    else:
        frequency[ele]=1
print(frequency)


dict1={"1":1,"2":2}
dict2={"3":3,"4":4}
merged_dict={**dict1,**dict2}
print(merged_dict)