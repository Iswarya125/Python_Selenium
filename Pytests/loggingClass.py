import inspect
import logging

class logging_base:
    def getlogger(self):
        #way to get the name of calling function
        testcase_name = inspect.stack()[1][3]
        logger = logging.getLogger(testcase_name)
        file_handler = logging.FileHandler("Output.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger