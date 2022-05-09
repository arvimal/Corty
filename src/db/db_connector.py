#!/usr/bin/env python3

import logging
import sys

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

HOST = "localhost"
PORT = "27017"

logger = logging.getLogger(__name__)


def mongo_conn():
    """
    Connect to the local MongoDB
    Create the local db `corty`, if it doesn't exist
    """
    corty_db = MongoClient()
    try:
        print(f"Connecting to MongoDB at {HOST}:{PORT}")
        res = corty_db.admin.command("ismaster")
        print(f"{res}")

    except ConnectionFailure as err:
        print("\nFailed to connect to MongoDB\n")
        print(f"- {err}")
        print("")
        print(" * Daisho requires an active MongoDB instance on localhost")
        print(" * Check if `mongod` service is running")
        sys.exit()
    return corty_db


def add_task(task_dict):
    """
    We conect to MongoDB here,
    to add our tasks
    """
    # Add the conector and note adder here
    print("\nTask added!")


def add_note(note_dict):
    """
    We conect to mongodb here,
    to add our notes
    """
    # Add the conector and note adder here
    logger.debug("Note added")
    print("\nNote added!")


if __name__ == "__main__":
    mongo_conn()
