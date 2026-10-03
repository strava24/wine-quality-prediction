# Logging is configured here because __init__.py runs once, the first time
# anything in the wineQualityML package is imported. This sets up logging
# before any other module runs, so every module can simply do
# `from wineQualityML import logger` and get the same format and handlers
# (file + stdout) without repeating the setup.
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("wineQualityML")