import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

logger = logging.getLogger("auction")