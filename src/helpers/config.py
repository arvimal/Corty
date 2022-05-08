#!/usr/bin/env python3

import configparser
import logging
import os
import pathlib

from src.client import cli
from src.db import db_connector
from src.helpers import help

HOME = os.getenv("HOME")
DAISHO_HOME = f"{HOME}/.config/corty/"
CONFIG = f"{DAISHO_HOME}corty.conf"
HISTORY = f"{DAISHO_HOME}history.txt"
LOG_FILE = f"{DAISHO_HOME}corty.log"

corty_logger = logging.getLogger(__name__)


class main(object):
    """ """

    def __init__(self):
        # Check existence of CONFIG
        if not all([pathlib.Path(CONFIG).exists(), pathlib.Path(LOG_FILE).exists()]):
            generate_config()
        else:
            corty_logger.info(f"{pathlib.Path(CONFIG)} exists, Welcome to Corty")
            print("\n\t- Welcome to Corty -\n")
            # Check if we are able to connect to MongoDB.
            db_connector.mongo_conn()
            cli.shell()
            logger.info("Started Corty prompt.")


def generate_config():
    # Check existence of CONFIG
    print("\n\t- Welcome to Corty -\n")
    print("Initial setup:")
    print("\tCreating Corty's configurations")

    # Create HOME, CONFIG, HISTORY, and LOG_FILE
    pathlib.Path(DAISHO_HOME).mkdir()
    pathlib.Path(CONFIG).touch(exist_ok=True)
    pathlib.Path(HISTORY).touch(exist_ok=True)
    pathlib.Path(LOG_FILE).touch(exist_ok=True)
    # Write Corty's configuration file
    conf_parser = configparser.ConfigParser()
    conf_parser.add_section("Global")
    conf_parser.set("Global", "DAISHO_HOME", DAISHO_HOME)
    conf_parser.set("Global", "CONFIG", CONFIG)
    conf_parser.set("Global", "HISTORY", HISTORY)
    conf_parser.set("Global", "LOG_FILE", LOG_FILE)
    with open(CONFIG, "w") as config_file:
        conf_parser.write(config_file)
    print("\tDone")

    # Configure logging from here
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
    logging.info("Generating configuration files.")
    logging.info("#### Corty starting up ####")
    # Check if we are able to connect to MongoDB.
    db_connector.mongo_conn()
    help.usage()
    cli.shell()
    logging.info("Started Corty prompt.")
