#!/usr/bin/env python3

import logging
import sys

import pymongo

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
        print("- {}".format(err))
        print("")
        print(" * Daisho requires an active MongoDB instance on localhost")
        print(" * Check if `mongod` service is running")
        sys.exit()
    return daisho_db


def add_task(task_dict):
    """
    We conect to MongoDB here,
    to add our tasks
    """
    # Add the conector and note adder here
    print("\nTask added!")
    pass


def add_note(note_dict):
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
