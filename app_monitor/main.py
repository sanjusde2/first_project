import logging 
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s---%(levelname)s---%(message)s--%(lineno)d")
logging.debug("I am enter into application")#1 
logging.info("you are login successfully")#2
logging.warning("there are 2items left")#3
logging.error("you ticket is not comfirmed due to payment failure")#4
logging.critical("too much traffic system crashed....")#5
logging.exception('yi code break ayindii')