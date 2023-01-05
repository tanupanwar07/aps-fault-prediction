import logging
import os
from datetime import datetime

#log file name
LOG_FILE=f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#log directory
LOG_File_directory=os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(LOG_File_directory,exist_ok=True)

#log file path
LOG_FILE_PATH= os.path.join(LOG_File_directory,LOG_File)

logging.basicConfig(
    filename="LOG_FILE",
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)