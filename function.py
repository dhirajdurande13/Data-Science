def positional_arguments(*numbers):
    for ele in numbers:
        print(ele,end=" ")
        
        
positional_arguments(1,2,3,4,5,"Rishi")


print()
def positional_keyword_arguments(**numbers):
    for key,value in numbers.items():
        print(f"{key} ->{value}",end=" ")
        
        
positional_keyword_arguments(name="Rishi",age=21,country="India")

'''argument and key-value both at same time'''

print()
def positional_keywordANDarguments(*args,**numbers):
    for ele in args:
        print(ele,end=" ")
    print()
    for key,value in numbers.items():
        print(f"{key} ->{value}",end=" ")
        
        
positional_keywordANDarguments(1,2,3,4,5,"MB",name="Rishi",age=21,country="India")




def multiplay(a,b):
    return a*b,a

print(multiplay(3,4))


# converting farnheight into celcius

# cheking week password

def check_password(password):
    if len(password)<8:
        return "Lower length"
    if not any(char.isdigit() for char in password):
        return "digit not present"
    if not any(char.islower() for char in password):
        return "lower letter not present"
    if not any (char.isupper() for char in password):
        return "upper letter not present"
    if not any(char in '@#$%&' for char in password):
        return "special char not present"
    else:
        return True
    
print(check_password("Rishi@13"))


def calculate_total_cost(cart):
    total=0
    for item in cart:
        total+=item['price']*item['quantity']
        
    return total

cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3}

]

## calling the function
total_cost=calculate_total_cost(cart)
print(total_cost)


def is_palindrome(str):
    str1=str.replace(' ','').lower()
    # print(str1)
    str2=str1[::-1]
    # print(str2)
    # print(str1)
    return str2==str1



print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))


# factorial

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

print(fact(5))
print(fact(7))



def count_frequency(filepath):
    with open(filepath,mode='r') as file:
        # content=file.read()
        wordcount={}
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                print(word)
                wordcount[word]=wordcount.get(word,0)+1
        # print(content)
        
        print(wordcount)
count_frequency('example1.csv')


import re
def validate_mail(mail):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    '''Function to validate email'''
    return re.match(pattern,mail) is not None

print(validate_mail("rishi@gmail.com"))
print(validate_mail("rishi@13"))