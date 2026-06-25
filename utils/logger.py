import logging
import os


def setup_logger():

    logger = logging.getLogger("PlaywrightLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        # Create folder if not exists
        os.makedirs("reports/logs", exist_ok=True)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        # Console Logs
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File Logs
        file_handler = logging.FileHandler(
            "reports/logs/test.log",
            mode="a"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger