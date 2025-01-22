import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s)')

PROJECT_NAME="cnnclassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/snippets.ipynb"   
]

for filepath in list_of_files:
    file_ = Path(filepath)
    dir_, filename = os.path.split(file_)

    if dir_ != "":
        os.makedirs(dir_, exist_ok=True)
        logging.info(f"Directory {dir_} for the file {file_} Succesfully Created")

    if (not os.path.exists(file_)) or (os.path.getsize(file_)):
        with open(filepath, "w") as f:
            pass

        logging.info(f"{file_} Successfully created")

    else:
        logging.info(f"{file_} is already exists")

