import logging

logging.basicConfig(filename='data_collector.info.log', encoding='utf-8', level=logging.INFO)
def get_logger(name):
    return logging.getLogger(name)