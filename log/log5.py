import logging

root_logger = logging.getLogger()
test_logger = logging.getLogger('test')

root_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

root_logger.addHandler(ch)
root_logger.addHandler(fh)
test_logger.addHandler(ch)

test_logger.propagate = False
test_logger.debug('dupa')
