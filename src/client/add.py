#!/usr/bin/env python3

"""
This module deals with adding notes and tasks,
as well as editing them later.
"""


import logging
import os
import pprint

from db import db_connector
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory


logger = logging.getLogger(__name__)
HOME = os.getenv("HOME")
CORTY_HOME = f'{HOME}/.config/corty/'
ADD_HISTORY = f'{CORTY_HOME}add_cmd.txt'


def add_prompt(job_type: str = None):
    """
    `add` accepts the following arguments.
        * task
        * note

    Example:
        ->> add task # To add a task to Corty.
        ->> add note # To add a note to Corty.
    """
    if job_type == "note":
        print(" - Creating a note.\n")
        note_fields = {
            "Subject": "",
            "Date": "",
            "Tags": [],
            "Priority": "",
            "Note": "",
        }
        for key in note_fields:
            note_fields[key] = prompt(
                "{:>10} : ".format(key), history=FileHistory(ADD_HISTORY)
            )
        print()
        corty_db.add_note(note_fields)
    elif job_type == "task":
        print(" - Creating a task.\n")
        task_fields = {"Subject": "", "Date": "", "Tags": [], "Priority": ""}
        for key in task_fields:
            task_fields[key] = prompt(
                "{:>10} : ".format(key), history=FileHistory(ADD_HISTORY)
            )
        print()
        corty_db.add_task(task_fields)


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
