


with open('example.csv',mode='r') as file:
    content=file.read()
    # file.
    # print(content)
    for line in content:
        print(line,end="")
    # .strip() remove the new line char
    
    
    
# If we use w mode for write this will write and overwrite the data inside that
# use append means a mode for write without overriding it 


# with open('example.csv',mode="a") as file:
#     file.write("\nThis is a new line with append!")


lst=["First line\n","Second Line\n","Third Line\n"]

# with open("example.txt",mode='a') as file:
#     for line in lst:
#         file.write(line)


with open('example.txt',mode='a') as file:
    file.writelines(lst)   #writing lst one time
    
    
    
# Working with binary files
# binary files which has data in bytes 
# extension with .bin

# use mode as a wb
data=b'\x00\x01\x011'
with open('example.bin',mode='wb') as file:
    file.write(data)
    
with open('example.bin',mode='rb') as file:
    content=file.read()
    print(content)
    
    
# with open('example.csv',mode='r') as file:
#     content=file.read()
# with open('example.txt',mode='a') as file:
#     file.write(content)


with open('example.csv',mode='r') as file:
    # content=file.read()
    lines=file.readlines()
    line_count=len(lines)
    word_count=sum(len(line.split()) for line in lines)
    char_count= sum(len(line) for line in lines)
    print(f"Lines: {lines} line_Count: {line_count} word_count {word_count} char count {char_count}")
   
   
   
#    w+ mode is a writing and reading if the file not exist new will created otherwise overwite

# when we want write and read at one time

with open('example1.csv',mode='w+') as file:
    file.write("This is new file named example1")
    file.write("\nThis is new one")
    file.seek(0)  #after writing move the cursor to the first line which is 0 index or at starting so that reading start from there
    # we read the file
    content=file.read()
    print(content)
    
    
# how to print full path with folder and file name

folder='mypackage'
file='module1.py'
import os

path=os.path.join(folder,file)
print(path)


# check the path exists or not

path='package'

if os.path.exists(path):
    print(f"Path Exists: {path}")
else:
    print(f"Path Does Not Exists: {path}")
    
    
# check path is file or directory

if os.path.isdir(path):
    print(f"Path is directory: {path}")
elif os.path.isfile(path):
    print(f"Path is file: {path}")
else:
    print(f"Path Not file or dir: {path}")
    
    
# relative path absolute path
relative_path='example.txt'
absolute_path=os.path.abspath(relative_path)
print(absolute_path)
