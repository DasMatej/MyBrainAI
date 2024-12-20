import logging
from logging import Formatter

class ColoredFormatter(Formatter):
    color_code = {
        'DEBUG': '\033[35m',  # Magenta
        'INFO': '\033[36m',  # Cyan
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',  # Red
        'CRITICAL': '\033[1;31m'  # Bold red
    }
    reset_code = '\033[0m'

    def format(self, record):
        log_msg = super().format(record)
        log_msg = log_msg.replace('\n', ' ')
        color_start = self.color_code.get(record.levelname, self.reset_code)
        return f'{color_start}{log_msg}{self.reset_code}'

def setup_logger(name=None):
    # create formatter
    formatter = ColoredFormatter(
        '%(asctime)s.%(msecs)03d] %(name)s.%(funcName)s() - %(levelname)s - %(filename)s - %(message)s',
        datefmt='%Y-%m-%d,%H:%M:%S')

    # configure logging for terminal
    console_handler = logging.StreamHandler()  # prints to terminal
    # DEBUG and above gets printed to the console
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # apply handlers to root logger
    logger = logging.getLogger(name)  # get a named logger
    logger.setLevel(logging.DEBUG)  # Set root logger level
    logger.addHandler(console_handler)

    return logger
