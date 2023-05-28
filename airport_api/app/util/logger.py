import logging

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # manipulador para definir o destino do log (console, arquivo, etc)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

logger = create_logger()