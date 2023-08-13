import os
import logging
from datetime import datetime

#file name is upto minutes
LOG_FILE_NAME=f"{datetime.now().strftime('%m_%d_%y_%H_%M')}.log"

#folder per day
LOG_FOLDER_NAME = f"{datetime.now().strftime('%y_%m_%d')}"

#create folders
LOG_PATH = os.path.join(os.getcwd(),"logs",LOG_FOLDER_NAME)
os.makedirs(LOG_PATH,exist_ok=True)

#file name for logging
LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level= logging.INFO,
    format="%(asctime)s, %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

#test logging
logging.info("Test Message")