
'''
Multiprocessing for CPU Bound task
factorial calculations
for large numbers involve significant calculation of work 
multiprocessing can be used to distribute the workload accroass multiple cpu cores


'''

import multiprocessing.pool
import sys
import multiprocessing
import time
import math
# Increasing the integer maximum conversion limit
sys.set_int_max_str_digits(100000)
def fact(n):
    print(f"Computing factorial of {n}")
    result=math.factorial(n)
    print(f"factorial of {n} is: {result}")
    return result


if __name__=='__main__':
    numbers=[2000,1200,1000,3000]
    start_time=time.time()
    # create a pool of workers
    with multiprocessing.Pool() as pool:
        results=pool.map(fact,numbers)
        
    end_time=time.time()
    
    print(f"Results is: {results}")
    print(f"Time taken: {end_time-start_time}")