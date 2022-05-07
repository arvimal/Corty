#!/usr/bin/env python3

import configparser
import logging
import os
import pathlib
import sys

# Workaround to set the `src` folder in PYTHONPATH
# to import `client` and subsequent functions
# Required, in pythonv3
cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
print(par_dir)
sys.path.append(par_dir)

from src.client import cli
from src.db import db_connector
from src.helpers import config, logger

if sys.version[0] != "3":
    print("\Requires Python v3")
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
        if all([pathlib.Path(CONFIG).exists()]):
            corty_logger.info(f"{pathlib.Path(CONFIG)} exists, Welcome to Corty")
            print("\n\t- Welcome to Corty -\n")
            # Check if we are able to connect to MongoDB.
            db_connector.mongo_conn()
            cli.shell()
            logger.info("Started Corty prompt.")

        else:
            config.generate_config()


if __name__ == "__main__":
    corty = main()
    corty.__init__()
