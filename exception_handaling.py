# handaling excdeptions using try,catch block

# try:
#     a=b
# except NameError as ex:
#     print(ex)



# FileNotFound: if file not present
# valueError : assigning value or syntax related error
# ZeroDivisionError: trying to divide by zero
try:
    x=10/11
    # a=b
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)
    # this main exception class should be defined at last only
# print(x)

# else block will execute whenever no error will happen means try executed succsesfully
# finally will execute at any cost wheteher error coming or not but it will not execute if compiler close or compiler exit
# try:
#     num=int(input("Enter number"))
#     div=10/num
# except ValueError:
#     print("enter valid number")
# except ZeroDivisionError:
#     print("Enter denominator greater than zero")
# else:
#     print(f"Division is: {div}")
    

try:
    with open('example1.csv',mode='r') as file:
        content=file.read()
        print(content)
except FileNotFoundError as ex:
    print(ex)
    print("No file error")
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print("File closed")
        print("Execution Succsessfull!")