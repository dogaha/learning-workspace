import logging

# configure logging, note only do this once
# filemode "w" will overwrite everything 
logging.basicConfig(level=logging.DEBUG, filename="logging/log.log",filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")

x = 2
logging.debug(f"the value of x is {x}")
logging.info("info")

# will print to console by default
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    1/0
except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError", exc_info=True) Does the same thing
    logging.exception("ZeroDivisionError")

# You can send http and emails with log
logger = logging.getLogger(__name__) #create new logger, save to diff file

#handler
handler = logging.FileHandler('logging/test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("test the custom logger")