#!/usr/bin/env python3

# Copyright (C) 2016 Vimal A.R <arvimal@yahoo.in>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import logging
import os

HOME = os.getenv('HOME')
DAISHO_HOME = HOME + "/.config/daisho/"
LOG_FILE = DAISHO_HOME + "daisho.log"

class Daisho_Logger:
    """
    Daisho's custom logger
    """
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p',
                    filename=LOG_FILE,
                    level=logging.INFO)
    daisho_logger = logging.getLogger("_daisho_")
    



