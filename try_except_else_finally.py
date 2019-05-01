import logging
print("import is successful")
import time
print("Time import is successful")
import math
print("math import is successful")
# Create Logger"
log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="/Users/sumon/pythonproblems.log", level=logging.DEBUG, format=log_format, filemode='w')
logger=logging.getLogger()
logger.info("Our test message 3")
print("Logging config is successful")
print(logger.level)
def read_file_timed(path):
    start_time = time.time()
