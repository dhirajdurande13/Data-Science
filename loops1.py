# num1=int(input("Enter num 1:"))
# num2=int(input("Enter num 2:"))
# op=input("Enter operator(+,-,*,/)")
# if op=='+':
#     print(num1+num2)
# elif op=='-':
#     print(num1-num2)
# elif op=='*':
#     print(num1*num2)
# elif op=='/':
#     print(num1/num2)
# else:
#     print("Valid character")

# age=int(input("Enter Your age:"))
# student=str(input("Are you a student yes/no:")).lower()

# if age<=5:
#     print("Free")
# elif age<=17:
#     if student=="yes":
#         print("10$")
#     else:
#         print("12$")
# elif age<=64:
#     if student=="yes":
#         print("15$")
#     else:
#         print("17$")
# else:
#     print("20$")



# Admin login system

# username="username"
# password="pass@123"

# inp_username=str(input("ENter Username:"))
# inp_password=str(input("Enter Password:"))

# if username==inp_username:
#     if(password==inp_password):
#         print("Authorized User")
#     else:
#         print("Incorrect Password")
        
# else:
#     print("Invalid username")

# for i in range(5,0,-1):
#     if i%2==0:
#         continue
#     print(i)
    
    
    
# # name="Rishi"
# # for i in name:
# #     print(i)

# for i in range(1,3,1):
#     for j in range(1,6,1):
#         print(f"i: {i} And j: {j}")


for i in range(2,20):
    flag=True
    # if i==2:
    #     print(i)
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
    if(flag==True):
        print(i)