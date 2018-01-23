#!/usr/bin/env python3

import logging

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
logging.info("#### Daisho starting up ####")
logging.info("{} exists".format(CONFIG))
