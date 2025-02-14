import inspect
import logging


def get_logger():
    log_name = inspect.stack()[1][3]
    logger = logging.getLogger(log_name)
    file_handler = logging.FileHandler(r"C:\Users\deepa\PycharmProjects\pythonProjectAppium\Appium_Framework1\log\generated_log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s",datefmt=
                                "%d/%m/%y  %I:%M:%S %p %M")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger








