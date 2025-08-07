
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), 'log', LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
def setup_logger(name):
    logger = logging.getLogger(name)    # Create a logger with the specified name
    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE_PATH)    # Create a file handler
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s') # Define the log format
        handler.setFormatter(formatter)   # Set the formatter for the handler
        logger.addHandler(handler)  # Add the handler to the logger
        logger.setLevel(logging.INFO)   # Set the logging level
    return logger

# Optional: test it directly
if __name__ == "__main__":
    log = setup_logger("test_logger")
    log.info("Logger is working!")
    print(f"Log written to: {LOG_FILE_PATH}")