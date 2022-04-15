import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="/home/ticvictech/PycharmProjects/PythonDemo/Logs/automation.txt", format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%y %I:%M:%S %P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
