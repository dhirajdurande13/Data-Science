# Multithreading
# when to use multithereding
# When I/O Bound task:Task that spend more time waiting for input output operations(File Operation,FIle request)
# WHen have to increase throuput of the application by increasing concurrent execution


import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers: {i}") 
        
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letters are :{letter}")
       
       
# we will createthe threads so that it will readuce the time # 
t=time.time()     
# print_number()
# print_letters()

t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letters)

# Need to start the thread
t1.start()
t2.start()
# It is going below without executing the thread that's why need to join that two threads so that after completing above execution only go below
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)