#!/usr/bin/env python3

import configparser
import logging
import os
import pathlib
from types import GeneratorType

from client import daisho_cli
from helpers import daisho_help
from server import daisho_db

HOME = os.getenv("HOME")
DAISHO_HOME = HOME + "/.config/daisho/"
CONFIG = DAISHO_HOME + "daisho.conf"
HISTORY = DAISHO_HOME + "history.txt"
LOG_FILE = DAISHO_HOME + "daisho.log"

daisho_logger = logging.getLogger(__name__)


def generate_config():
    # Check existence of CONFIG
    print("\n\t- Welcome to Daisho -\n")
    print("Initial setup:")
    print("\tCreating Daisho's configurations")

    # Create HOME, CONFIG, HISTORY, and LOG_FILE
    pathlib.Path(DAISHO_HOME).mkdir()
    pathlib.Path(CONFIG).touch(exist_ok=True)
    pathlib.Path(HISTORY).touch(exist_ok=True)
    # pathlib.Path(LOG_FILE).touch(exist_ok=True)
    # Write Daisho's configuration file
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
    logging.info("#### Daisho starting up ####")
    # Check if we are able to connect to MongoDB.
    daisho_db.mongo_conn()
    daisho_help.usage()
    daisho_cli.shell()
    logging.info("Started Daisho prompt.")
