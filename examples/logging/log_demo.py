
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Logging started!")
logging.warning("Warning!!!")

# Modify format
logging.basicConfig(filename="log.txt", format="%(levelname)s:%(asctime)s:%(message)s", force=True)
logging.warning("This is warning!")