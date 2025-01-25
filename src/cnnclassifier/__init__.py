import logging
from pathlib import Path
import os
import sys

logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

dir_ = "logs"
logs_file_path = os.path.join(dir_, "running_logs.log")
os.makedirs(Path(dir_), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(logs_file_path),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger("cnnclassifierlogger")