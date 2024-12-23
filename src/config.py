import os

SEED = 73


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
OUPUT_DIR = os.path.join(PROJECT_DIR, "output")
MODEL_DIR = os.path.join(PROJECT_DIR, "model")
LOG_DIR = os.path.join(PROJECT_DIR, "log")
