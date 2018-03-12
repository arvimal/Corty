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
from prompt_toolkit.history import FileHistory
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit import prompt
from daisho_db import mongo_conn, mongo_add_note, mongo_add_task
# Remove this at last, if only used for printing debug output.
import pprint 

HOME = os.getenv('HOME')
DAISHO_HOME = HOME + "/.config/daisho/"
ADD_HISTORY = DAISHO_HOME + "add_cmd.txt"


def add_prompt(self, job_type=None):
    """
    Adds your tasks
    """
    if job_type == "task":
        task_fields = {
            "Subject": "",
            "Date": "",
            "Tags": [],
            "Priority": ""
        }
        print(" - Creating a task.\n")
        for key in task_fields:
            task_fields[key] = prompt("{:>10} : ".format(
                key), history=FileHistory(ADD_HISTORY))
        print()
        add_task(task_fields)

    elif job_type == "note":
        note_fields = {
            "Subject": "",
            "Date": "",
            "Tags": [],
            "Priority": "",
            "Note": ""
        }
        print(" - Creating a note.\n")
        for key in note_fields:
            note_fields[key] = prompt("{:>10} : ".format(
                key), history=FileHistory(ADD_HISTORY))
        print()
        add_note(note_fields)
    # Process the dict `fields` before sending to
    # mongodb via add_data()
    else:
        # add_prompt(self, job_type)
        pass

def add_task(task_dict):
    """
    Add tasks entries in the db
    """
    pprint.pprint(task_dict)
    print("Adding your task to the database!")
    mongo_add_task(task_dict)

def add_note(note_dict):
    """
    Add note entries in the db
    """
    # Cleanup: Remove print() and set logger here.
    pprint.pprint(note_dict)
    # Cleanup: Remove print() and set logger here. 
    print("Adding your note to the database!")
    mongo_add_note(note_dict)
