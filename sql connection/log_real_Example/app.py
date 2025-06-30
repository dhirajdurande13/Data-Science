import logging


logging.basicConfig(
    # filename="app.log",
    # filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)


logger=logging.getLogger('ArithmaticApp')



def add(a,b):
    result=a+b
    logger.debug(f'Addition of {a}+{b} debug')
    return result
def sub(a,b):
    result=a-b
    logger.debug(f'subtraction of {a}-{b} debug')
    return result
def mult(a,b):
    result=a*b
    logger.debug(f'Multiplication of {a}*{b} debug')
    return result
def divide(a,b):
    try:
        result=a/b
        logger.debug(f'Division of {a}/{b} debug')
        return result
    except ZeroDivisionError as e:
        logger.error('Zero division error')
        return None
    
    
print(add(10,15))
print(sub(15,10))
print(mult(10,5))
print(divide(15,0))