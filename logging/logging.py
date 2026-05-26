import logging

logging.basicConfig(level=logging.INFO, filename="log.log",filemode="w")

logging.debug("debug")
logging.info("info")

# will print to console
logging.warning("warning")
logging.error("error")
logging.critical("critical")
