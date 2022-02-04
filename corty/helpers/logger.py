#!/usr/bin/env python3

import logging
import os

HOME = os.getenv("HOME")
DAISHO_HOME = HOME + "/.config/daisho/"
LOG_FILE = DAISHO_HOME + "daisho.log"


class Daisho_Logger:
    """
    Daisho's custom logger
    """

    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%m-%d-%Y %I:%M:%S %p",
        filename=LOG_FILE,
        level=logging.INFO,
    )
    daisho_logger = logging.getLogger("_daisho_")
