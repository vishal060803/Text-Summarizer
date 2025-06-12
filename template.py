import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",# CD/CI Intergration
    f"src/{project_name}/__init__.py",# Used to import Global Variables
    f"src/{project_name}/components/__init__.py",# Used to import components
    f"src/{project_name}/utils/__init__.py",# Used to import utils
    f"src/{project_name}/utils/common.py",# Common functions
    f"src/{project_name}/logging/__init__.py",# Logger configuration
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",# Configuration file
    f"src/{project_name}/pipeline/__init__.py",# Pipeline for the project
    f"src/{project_name}/entity/__init__.py",# Configuration file
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",# Configuration file
    "params.yaml",# Parameters file
    "app.py",# Main application file
    "main.py",# Main entry point
    "Dockerfile",# Dockerfile for containerization
    "requirements.txt",# Requirements file
    "setup.py",# Setup file for packaging"
    "research/trials.ipynb",# Jupyter notebook for trials

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # Split the path into directory and file name

    if filedir != "":# If the directory is not empty, create the directory
        os.makedirs(filedir, exist_ok=type)# Create the directory if it does not exist
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):# If the file does not exist or is empty, create an empty file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else: 
        logging.info(f"{filename} is already exists")