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

from client import cli
from helpers import config, help, logger
from server import db

if sys.version[0] != "3":
    print("\Requires Python v3")
    print("Exiting!\n")
    sys.exit(1)

HOME = os.getenv("HOME")
CORTY_HOME = HOME + "/.config/corty/"
CONFIG = CORTY_HOME + "corty.conf"
HISTORY = CORTY_HOME + "history.txt"
LOG_FILE = CORTY_HOME + "daisho.log"
daisho_logger = logging.getLogger(__name__)


class main(object):
    """ """

    def __init__(self):
        # Check existence of CONFIG
        if all([pathlib.Path(CONFIG).exists()]):
            daisho_logger.info(
                "{} exists, Welcome to Daisho".format(pathlib.Path(CONFIG))
            )
            print("\n\t- Welcome to Daisho -\n")
            # Check if we are able to connect to MongoDB.
            daisho_db.mongo_conn()
            daisho_cli.shell()
            daisho_logger.info("Started Daisho prompt.")

        else:
            daisho_config.generate_config()


if __name__ == "__main__":
    corty = main()
    corty.__init__()
