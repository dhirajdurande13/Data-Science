import logging

# defining the logging levels
# logging.basicConfig()
# logging.basicConfig(level=logging.DEBUG)
# # logging message
# logging.error("Error Message")
# logging.warning("Warning Message")
# logging.critical("Critical Message")

# print("Details with Format")

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

# logging.error("Error Message")
# logging.warning("Warning Message")
# logging.critical("Critical Message")


# will tray to add in file
logging.basicConfig(
    filename="app.log",
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.error("Error Message")
logging.warning("Warning Message")
logging.critical("Critical Message")