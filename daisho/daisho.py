#!/usr/bin/env python3

# MIT License

# Copyright (C) 2021 Vimal A.R <arvimal81@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

from daisho.client import daisho_cli
from daisho.helpers import daisho_config
from daisho.server import daisho_db

if sys.version[0] != "3":
    print("\nDaisho requires Python v3")
    print("Exiting!\n")
    sys.exit(1)

HOME = os.getenv("HOME")
DAISHO_HOME = HOME + "/.config/daisho/"
CONFIG = DAISHO_HOME + "daisho.conf"
HISTORY = DAISHO_HOME + "history.txt"
LOG_FILE = DAISHO_HOME + "daisho.log"
daisho_logger = logging.getLogger(__name__)


class Daisho(object):
    """Daisho's main class"""

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
    my_daisho = Daisho()
    my_daisho
