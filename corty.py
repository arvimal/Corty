#!/usr/bin/env python3

import configparser
import logging
import os
import pathlib
import sys

from src.client import cli
from src.db import db_connector
from src.helpers.config import generate_config

if sys.version[0] != "3":
    print("\nRequires Python v3")
    print("Exiting!\n")
    sys.exit(1)

HOME = os.getenv("HOME")
CORTY_HOME = f"{HOME}/.config/corty/"
CONFIG = f"{CORTY_HOME}corty.conf"
HISTORY = f"{CORTY_HOME}history.txt"
LOG_FILE = f"{CORTY_HOME}corty.log"
corty_logger = logging.getLogger(__name__)


class main(object):
    """ """

    def __init__(self):
        # Check existence of CONFIG
        if all([pathlib.Path(CONFIG).exists(), pathlib.Path(LOG_FILE).exists]):
            generate_config()
        else:
            corty_logger.info(f"{pathlib.Path(CONFIG)} exists, Welcome to Corty")
            print("\n\t- Welcome to Corty -\n")
            # Check if we are able to connect to MongoDB.
            db_connector.mongo_conn()
            cli.shell()
            logger.info("Started Corty prompt.")


if __name__ == "__main__":
    corty = main()
    corty.__init__()
