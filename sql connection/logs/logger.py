import logging

logging.basicConfig(
    filename="apps.log",
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# logging.error("Error Message")
# logging.warning("Warning Message")
# logging.critical("Critical Message")