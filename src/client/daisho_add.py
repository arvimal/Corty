#!/usr/bin/env python3

# MIT License

# Copyright (C) 2018 Vimal A.R <arvimal@yahoo.in>

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

"""
This module deals with adding notes and tasks,
as well as editing them later.
"""

import logging
import os
import pprint

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory

from client import daisho_db

logger = logging.getLogger(__name__)
HOME = os.getenv("HOME")
DAISHO_HOME = HOME + "/.config/daisho/"
ADD_HISTORY = DAISHO_HOME + "add_cmd.txt"


def add_prompt(job_type=None):
    """
`add` accepts the following arguments.
    * task
    * note

Example:
    ->> add task # To add a task to Daisho.
    ->> add note # To add a note to Daisho.
    """
    if job_type == "task":
        task_fields = {"Subject": "", "Date": "", "Tags": [], "Priority": ""}
        print(" - Creating a task.\n")
        for key in task_fields:
            task_fields[key] = prompt(
                "{:>10} : ".format(key), history=FileHistory(ADD_HISTORY)
            )
        print()
        daisho_db.add_task(task_fields)

    elif job_type == "note":
        note_fields = {
            "Subject": "",
            "Date": "",
            "Tags": [],
            "Priority": "",
            "Note": "",
        }
        print(" - Creating a note.\n")
        for key in note_fields:
            note_fields[key] = prompt(
                "{:>10} : ".format(key), history=FileHistory(ADD_HISTORY)
            )
        print()
        daisho_db.add_note(note_fields)
    # Process the dict `fields` before sending to
    # mongodb via add_data()
    else:
        # add_prompt(self, job_type)
        pass


def add_task(task_dict):
    """
    Add tasks entries in the db
    """
    print(task_dict)
    print("Adding your task to the database!")


def add_note(note_dict):
    """
    Add note entries in the db
    """
    # Cleanup: Remove print() and set logger here.
    pprint.pprint(note_dict)
    # Cleanup: Remove print() and set logger here.
    print("Adding your note to the database!")


def edit_prompt(job_type=None, element_number=None):
    pass
