import logging
from datetime import datetime

now = datetime.now()

def create_logging_debug(local):

    logger = logging.getLogger(local)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s : %(message)s')

    dt_string = now.strftime('%d%m%Y%H_%M_%S')
    print(dt_string)

    file_handler = logging.FileHandler('log/L{}.log'.format(str(dt_string)))
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

