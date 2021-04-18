import logging

def test_logging_Demo():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("Output.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("error message")
    logger.critical("critical message")


