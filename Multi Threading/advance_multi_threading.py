# Thread poll executor
# even there is sleep it  will execute witout taking too much of time
from concurrent.futures import ThreadPoolExecutor
import time
def print_numbers(number):
    time.sleep(1)
    return f"Numbers: {number}"

numbers=[1,2,3,4,5,6,7,11,12,13,14,15,11,1,1,10]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,numbers) 
    
for result in results:
    print(result)