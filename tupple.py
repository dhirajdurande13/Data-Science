

tpl=tuple(range(1,11))
print(tpl)


print(tpl[0])
print(tpl[len(tpl)//2])
print(tpl[-1])


print(tpl[:3])
print(tpl[-3:])
print(tpl[2:6])


matrix=(
    (1,2,3),
    (11,21,31),
    (12,22,32)
    
)

for row in matrix:
    print(row)
    
print(matrix[1][2])

tpl1=(1,2,3,4)
tpl2=(11,12,13,14)

print(tpl1+tpl2)

tpl3=(1,2,3,4,1,1,2,2,3,3)
print(tpl3.count(2))
print(tpl3.index(3))


a,b,c,d=tpl1
print(a,b,c,d)

lst=[1,2,3,4,5]
print(tuple(lst))
lst1=list(tpl2)
lst1.append(6)

print(tuple(lst1))

str="Hello"
tpl4=tuple(str)
print(tpl4)
joined_string=''.join(tpl4)
print(joined_string)


tpl_dict={
    1:(2,3),
    2:(3,4),
    4:(5,6)
}
print(tpl_dict)

for row in matrix:
    for ele in row:
        print(ele,end=" ")
    print()
    
    
print(set(tpl3))


tpl=(1,2,3,4,5)
print(min(tpl))
print(max(tpl))
print(sum(tpl))


st=set(range(1,11))
print(st)
st.add(34)
print(st)
st.remove(5)
print(st)

st1=set()
st2=set()
for i in range(1,6):
    st1.add(i)
    
for i in range(1,11):
    if(i%2==0):
        st2.add(i)
        
print(st1)
print(st2)
print(st1 | st2)
print(st1 & st2)
print(st1 - st2)
print(st1 ^ st2)

st3={x:x**2 for x in range(1,11)}
print(st3)

st4={x for x in st if x%2==0}
print(st4)


st5=set(range(1,6))
st6=set(range(1,3))
print(st6.issubset(st5))
print(st5.issuperset(st6))


# frozenset
st7=frozenset(range(1,6))
print(st7)


d={
    "s1":{1,2,3,4},
    "s2":{11,21,31,41},
    "s3":{11,12,13,41},
    "s4":{13,2,3,4}
}
print(d)

st9={1,2,3,4,5}

while st9:
    st9.pop()
    
print(st9)


print(3 in st5)
print(8 in st5)


st10={(1,2),(3,4),(5,6)}
print(st10)


dict={x:x**2 for x in range(1,11)}
print(dict)
print(dict[5])
print(dict.keys())
dict[11]=121
print(dict)
dict.pop(1)
print(dict)


# for key,values in dict.items():
#     print(key,values)


dict1={x:x*x*x for x in range(1,10)}
print(dict1)

dict2={
    "Name":"Rishi",
    "Age":34
}
dict.update(dict2)
print(dict)

dict3={
    "l1":[1,2,3],
    "l2":[4,4,5]
}
print(dict3)


print(list(dict1.items()))

dict3={x:x**2 for x in range(1,11) if x%2==0}
print(dict3)

swaped_dict={v:x for x,v in dict3.items()}
print(swaped_dict)


from collections import defaultdict
defaultdict=defaultdict(list)
defaultdict['a'].append(1)
defaultdict['b'].append(2)
defaultdict['c'].append(3)
print(defaultdict)


str="Hello Word"

def count_char(str):
    char_dict={}
    for ch in str:
        char_dict[ch]=char_dict.get(ch,0)+1
    return char_dict
        
print(count_char(str))
        
        
        
book={
    "Name":"chava",
    "Author":"Shivaji sawant",
    "Genre":"Historical",
    "Copies":20
}

print(book)
import json
book1=json.dumps(book)
print(json.dumps(book))
print(type(book1))



