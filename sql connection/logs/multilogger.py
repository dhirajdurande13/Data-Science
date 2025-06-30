import logging

# For Module 1
loger1=logging.getLogger("Module 1")
loger1.setLevel(logging.DEBUG)

# For Module 2
logger2=logging.getLogger("Module 2")
logger2.setLevel(logging.WARNING)

logging.basicConfig(
    
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# THis is all for if we consider 1 module it will give root
# IF we define as a model it will give Module1 or Module 2

loger1.debug("THis is debug Message for Module 1")
logger2.warning("THis is warning Message for Module 2")
