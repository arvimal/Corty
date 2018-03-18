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

import pymongo
import sys
import logging

HOST = "localhost"
PORT = "27017"

logger = logging.getLogger(__name__)


def mongo_conn():
    """
    Connect to the local MongoDB
    Create the local db `daisho`, if it doesn't exist
    """
    try:
        connect = pymongo.MongoClient(HOST + ":" + PORT)
        # Connect to the `daisho` db (will create if non-existing)
        daisho_db = connect.daisho
        if connect.database_names():
            pass

    except pymongo.errors.ConnectionFailure as err:
        print("\nFailed to connect to MongoDB\n")
        print(" * ERROR:- {}".format(err))
        print("")
        print(" * Daisho requires an active MongoDB instance on localhost")
        print(" * Check if `mongod` service is running")
        sys.exit()
    return daisho_db


def mongo_add_task(task_dict):
    """
    We conect to MongoDB here,
    to add our tasks
    """
    # Add the conector and note adder here
    print("\nTask added!")
    pass


def mongo_add_note(note_dict):
    """
    We conect to mongodb here,
    to add our notes
    """
    # Add the conector and note adder here
    logger.debug("Note added")
    print("\nNote added!")
    pass


if __name__ == "__main__":
    mongo_conn()
