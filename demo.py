from us_visa import logging
from us_visa import CustomException
import sys

#logging.info("welcome to our custom log")

try:
    a = 2/0
except Exception as e:
    raise CustomException(e, sys)