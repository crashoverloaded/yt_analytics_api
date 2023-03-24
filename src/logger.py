
import logging as lg
import os
from datetime import datetime

# creating a log file name based on date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path of log file
logs_path = os.path.join(os.getcwd(),"logs")

# Exist_ok = True is set to append the file and folder as per need  hence no need to create the structure again and again
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

lg.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=lg.INFO
)

# testing the logging file
if __name__ == "__main__":
    lg.info("Logging has started")