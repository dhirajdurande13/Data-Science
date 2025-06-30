# Processes that runs parllely
# #CPU BOUND TASK : That are heavy to do in terms of CPU (Mathematical Computation)

# Parllel Execution:when have to use multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"{i}-> {i*i}")
        
        
        
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"{i}-> {i*i*i}")
        
 
t1=time.time() 

#ENtry point for process entire execution will start here
if __name__=='__main__':
    p1=multiprocessing.Process(target=square_numbers)      
    p2=multiprocessing.Process(target=cube_numbers)
    p1.start()
    p2.start()

# Wait for the process to complete
    p1.join()
    p2.join()      
    print(time.time()-t1)