import inspect
import logging

def get_logger():
    log_name = inspect.stack()[1][3]
    logger = logging.getLogger(log_name)
    file_handler = logging.FileHandler("My log")
    Formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    file_handler.setFormatter(Formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
