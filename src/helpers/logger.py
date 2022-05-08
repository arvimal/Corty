#!/usr/bin/env python3

import logging
import os

HOME = os.getenv("HOME")
DAISHO_HOME = f"{HOME}/.config/corty/"
LOG_FILE = f"{DAISHO_HOME}corty.log"


class Corty_Logger:
    """
    Corty's custom logger
    """

    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%m-%d-%Y %I:%M:%S %p",
        filename=LOG_FILE,
        level=logging.INFO,
    )
    corty_logger = logging.getLogger("_corty_")
