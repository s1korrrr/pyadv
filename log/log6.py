import logging
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s %(message)s'
)
resp = requests.get('http://www.google.pl/')
logging.info(resp)