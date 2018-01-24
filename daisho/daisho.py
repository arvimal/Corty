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
import pathlib
import configparser
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
import daisho_db
import daisho_logger
import sys
if sys.version[0] != "3":
    print("\nDaisho requires Python v3.")
    print("Install Python v3, or use the v3 binary to run `daisho.py` if already installed.")
    print("\n\t# python3.6 daisho.py\n")
    print("Exiting Daisho!\n")
    sys.exit(1)


HOME = os.getenv('HOME')
DAISHO_HOME = HOME + "/.config/daisho/"
CONFIG = DAISHO_HOME + "daisho.conf"
HISTORY = DAISHO_HOME + "history.txt"
LOG_FILE = DAISHO_HOME + "daisho.log"


class Daisho(object):
    """Daisho's main class"""

    def __init__(self):
        # Check existence of CONFIG
        # Move logging to its own file
        if all([pathlib.Path(CONFIG).exists()]):

            print("\n- Welcome to Daisho -\n")
            # Check if we are able to connect to MongoDB.
            daisho_db.mongo_conn()
            self.daisho_help()
            self.daisho_prompt()
            logging.info("Started Daisho prompt.")

        else:
            print("\n- Welcome to Daisho -\n")
            print("Initial setup:")
            print("\tCreating Daisho's configurations")

            # Create HOME, CONFIG, HISTORY, and LOG_FILE
            pathlib.Path(DAISHO_HOME).mkdir()
            pathlib.Path(CONFIG).touch(exist_ok=True)
            pathlib.Path(HISTORY).touch(exist_ok=True)
            pathlib.Path(LOG_FILE).touch(exist_ok=True)
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
            self.daisho_help()
            self.daisho_prompt()
            logging.info("Started Daisho prompt.")

    def daisho_help(self):
        """
        Daisho's Usage
        """
        print("\nUsage:")
        print(" 1. add <to-do>          - Add a new to-do.")
        print(" 2. search <key-word>    - Search for a keyword.")
        print(" 3. list <day>           - List to-dos for the day.")
        print(" 4. help                 - Prints this help message. ")
        print(" 5. quit                 - Quits Daisho. \n")
        pass

    def daisho_prompt(self):
        """
        Daisho's prompt.
        """
        cmd_list = [
            'add',
            'list',
            'search',
            'help',
            'quit'
        ]
        keyword_completer = WordCompleter(cmd_list)

        while True:
            daisho_prompt = prompt("daisho ->> ",
                                   history=FileHistory(HISTORY),
                                   auto_suggest=AutoSuggestFromHistory(),
                                   completer=keyword_completer)
            # Split the input to a list
            value = daisho_prompt.split(" ")
            # Branch out based on inputs
            if value[0] == 'add':
                self.add_tasks()
            elif value[0] == 'list':
                self.list_tasks(value)
            elif value[0] == 'search':
                self.search_tasks(self, value)
            elif value[0] == 'help':
                self.daisho_help()
            elif value[0] == 'quit':
                sys.exit("\nExiting Daisho.\n")
            else:
                self.daisho_help()

    def list_tasks(self, value="today"):
        """
        List tasks based on dates and fuzzy inputs,
        Ex: today, tomorrow, yesterday, date etc.
        """
        print(self.list_tasks.__doc__)
        logging.info("Calling list_tasks()")
        pass

    def search_tasks(self, *args):
        """
        Search tasks based on keywords
        """
        print(self.search_tasks.__doc__)
        logging.info("Calling search_tasks()")
        pass


if __name__ == "__main__":
    my_daisho = Daisho()
    my_daisho()
