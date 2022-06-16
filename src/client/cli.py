#!/usr/bin/env python3

import logging
import os
import sys

from src.helpers import help
from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory

from src.client import add, list

# from prompt_toolkit.shortcuts import ProgressBar
# from pygments.token import Token


HOME = os.getenv("HOME")
DAISHO_HOME = f"{HOME}/.config/corty/"
CONFIG = f"{DAISHO_HOME}corty.conf"
HISTORY = f"{DAISHO_HOME}history.txt"
LOG_FILE = f"{DAISHO_HOME}corty.log"
corty_logger = logging.getLogger(__name__)


def shell():
    """
    Corty's prompt.
    """
    cmd_list = ["add", "del", "list", "find", "edit", "open", "help", "quit"]
    keyword_completer = WordCompleter(cmd_list, ignore_case=True)

    while True:
        corty_prompt = prompt(
            "corty ->> ",
            history=FileHistory(HISTORY),
            auto_suggest=AutoSuggestFromHistory(),
            completer=keyword_completer,
        )
        # Split the input to a list
        values = list(corty_prompt.split())  # type: ignore
        key_word = values[0].lower()

        if key_word in cmd_list:
            # Case 1: key_word is `help` / `quit` / `list`
            # `help` and `quit` are cases where a single arg is valid.
            # `list` without args should list all tasks and notes [Feature]
            if len(values) == 1:
                if key_word == "help":
                    help.usage()
                elif key_word == "quit":
                    sys.exit("\nExiting Corty.\n")
                elif key_word == "list":
                    list.list_tasks(val="all")
                else:
                    help.usage()
                    shell()

            elif len(values) > 1:
                # Case 2: key_word is "add"
                if key_word == "add":
                    add_args = ["note", "task"]
                    if values[1].lower() in add_args:
                        add.add_prompt(job_type=values[1].lower())
                        help.usage()
                    else:
                        print(add.add_prompt.__doc__)
                        shell()

                # Case 3: key_word is "list"
                if key_word == "list":
                    list_args = ["all", "today", "tags", "prio", "trash"]
                    if values[1].lower() in list_args:
                        list.list_tasks(val=values[1].lower())
                    else:
                        print(list.list_tasks.__doc__)
                        shell()

                # Case 4: key_word is "edit"
                if key_word == "edit":
                    edit_args = ["task", "note"]
                    if values[1].lower() in edit_args:
                        try:
                            if values[2]:
                                try:
                                    job_type, num = (
                                        values[1].lower(),
                                        int(values[2]),
                                    )
                                    edit_jobs(job_type=job_type, number=num)
                                except ValueError:
                                    print(edit_jobs.__doc__)
                                    shell()
                        except IndexError:
                            print(edit_jobs.__doc__)
                            shell()
                    else:
                        # print("`edit` takes either `task` or `note` as argument.")
                        print(self.edit_jobs.__doc__)
                        shell()

                # Case 5: key_word is "open"
                if key_word == "open":
                    open_args = ["task", "note"]
                    if values[1].lower() in open_args:
                        try:
                            if values[2]:
                                try:
                                    job_type, num = (
                                        values[1].lower(),
                                        int(values[2]),
                                    )
                                    self.open_jobs(job_type=job_type, number=num)
                                except ValueError:
                                    print(self.open_jobs.__doc__)
                                    shell()
                        except IndexError:
                            print(self.open_jobs.__doc__)
                            shell()
                    else:
                        # print("`edit` takes either `task` or `note` as argument.")
                        print(self.open_jobs.__doc__)
                        shell()

        else:
            # if values[0].lower() not in list
            corty_help.usage()
