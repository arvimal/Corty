#!/usr/bin/env python3

"""
This module deals with adding notes and tasks,
as well as editing them later.
"""

import logging
import os
import pprint

from corty.db import db_connector
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory

from server import daisho_db

logger = logging.getLogger(__name__)
HOME = os.getenv("HOME")
DAISHO_HOME = HOME + "/.config/daisho/"
ADD_HISTORY = DAISHO_HOME + "add_cmd.txt"


def add_prompt(job_type: str = None):
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
