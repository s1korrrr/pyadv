import logging
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s %(message)s'
)

url_logger = logging.getLogger(
    'urllib3.connectionpool'
)

url_logger.setLevel(logging.INFO)
resp = requests.get('http://www.google.pl/')
logging.log(30, resp)