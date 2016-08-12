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

import os
import sys
import yaml
import ConfigParser
import logging


DAISHO_HOME = "~/.config/daisho/"
CONFIG = "~/.config/daisho/daisho.conf"
TODO_LIST = "~/.config/daisho/to-do.yaml"


class Daisho(object):
    """The main class"""

    def __init__(self):
        if os.path.exists(TODO_LIST) and os.path.exists(CONFIG):
            self.daisho_prompt()
        else:
            print("\nWelcome to Daisho.")
            print("\nInitial setup...")
            print("This is a one-time task.\n")
            print("Creating Daisho's config directory.")
            os.mkdir(DAISHO_HOME)
            print("Creating configuration files.\n")
            daisho_config_file = ConfigParser.ConfigParser()

    def daisho_prompt(self):
        """The heart of Daisho"""
        while True:
            prompt = raw_input("daisho ->> ")
            value = prompt.split(" ")
            if len(value) == 1 and value[0] == "add":
                print("`add` takes a to-do, try again!")

            elif len(value) >= 1 and value[0] == "add":
                self.add_tasks()

            if len(value) == 1 and value[0] == "list":
                self.list_tasks()

            elif value[0] == "search":
                # We call the __doc__ magic method till it's implemented.
                print(self.search_tasks.__doc__)

            elif value[0] == "quit":
                sys.exit("\nExisting pytick!\n")

            else:
                self.daisho_help()

    def list_tasks(self):
        """Lists tasks.
        Takes arguments such as `today`, `tomorrow`, weekday etc..

        Not yet implemented, come again later!
        """
        pass

    def add_tasks(self, *args):
        # Add tasks as yaml
        pass

    def search_tasks(self):
        """Search tasks based on keywords"""
        print("Not yet implemented, come again later!")
        pass

    def daisho_help(self):
        """Usage:"""


my_daisho = Daisho()
my_daisho.daisho_prompt()
