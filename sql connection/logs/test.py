
from logger import logging

def add(a,b):
    logging.debug("Add Function Called")
    return a+b

logging.debug("Debugging outside the function")
print(add(4,5))