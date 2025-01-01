import os

SEED = 73


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
OUPUT_DIR = os.path.join(PROJECT_DIR, "output")
MODEL_DIR = os.path.join(PROJECT_DIR, "model")
LOG_DIR = os.path.join(PROJECT_DIR, "logs")

NUM_TRAILS = 200
TARGET = ""
PARTITION_DIM = ""  # Dimension which defines the splits of dims

EDA_CONIG = {}


FEATURE_CONFIG = {}


INTERMITTENT_CONFIG = {"models": [], "metric": [], "inference": []}


MODEL_CONFIG = {"models": [], "metric": []}

NEW_PRODUCT_CONFIG = {"models": []}
