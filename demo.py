from PredictUSVissaApproval.logger import logging

# logging.info("Welompe to our coustom log")


#----------------------------------------------------------------

from PredictUSVissaApproval.exception import USvisaException
import sys

try:
    a = 1/ "10"
except Exception as e:
    # logging.info(e)
    raise USvisaException(e, sys) from e


#----------------------------------------------------------------