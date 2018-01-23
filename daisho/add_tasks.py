#!/usr/bin/env python3

from prompt_toolkit.history import FileHistory
from prompt_toolkit.contrib.completers import WordCompleter
import daisho_db


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
        fields[key] = input("{0:10} : ".format(key))
    # print(fields)  # Added for self info
    print()
    # Process the dict `fields` before sending to
    # mongodb via daisho_db.add_data()

    pass
