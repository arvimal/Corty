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

from prompt_toolkit.history import FileHistory
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit import prompt
import daisho_db

ADD_HISTORY = "/tmp/add_cmd.txt"


def add_tasks(self):
    """
    Adds your tasks
    """
    fields = {
        "Subject": "",
        "Date": "",
        "Tags": "",
        "Priority": ""
    }

    for key in fields:
        fields[key] = prompt("{0:10} : ".format(
            key), history=FileHistory(ADD_HISTORY))
    # print(fields)  # Added for self info
    print()
    # Process the dict `fields` before sending to
    # mongodb via daisho_db.add_data()

    pass
