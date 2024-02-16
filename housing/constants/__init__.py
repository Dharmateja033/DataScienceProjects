import os
from datetime import datetime

ROOT_DIR = os.getcwd()

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,'config','config.yaml')
CURR_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
