#!/usr/bin/env python3

"""
corty_list handles listing the tasks and notes, based on filters.

`filters` are any one of the following:

* all [default]
* today
* tomorrow
* date [`DD-MM-YYYY`]
* tags [#tag_val]
* prio [#high, #med, #low]
* trash

This also takes care on opening tasks which has active sub-tasks,
as well as notes in the pre-configured editor of your choice.
"""

from db import db_connector


def list_tasks(val: str = "all"):
    """
    `list` accepts the following arguments:
        * all
        * today
        * date, in `DD-MM-YYYY` format
        * tags
        * prio
        * trash
    """
    # print("List called with argument `{}`".format(val))
    # TODO: `trash`, `tags`, prio` not in initial implementation
    # TODO: Initial implementation only carries `all`, `today`, `date`
    if val == "today":
        print("Listing today's tasks")
        # corty_db.sys(search.today)
    elif val == "all":
        print("Listing all tasks")
        # corty_db.sys(search.tomorrow)
    elif val == "prio":
        print("Listing tasks sorted on priority")
    elif val == "tags":
        print("Listing tasks based on tags")
