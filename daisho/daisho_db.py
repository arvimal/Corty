#!/usr/bin/env python3

import pymongo
import sys

HOST = "localhost"
PORT = "27017"


def mongo_conn():
    """
    Connect to the local MongoDB
    Create the local db `daisho`, if it doesn't exist
    """
    print("\nTrying to connect to MongoDB on {}".format(HOST, PORT))
    try:
        connect = pymongo.MongoClient(HOST + ":" + PORT)
        # Connect to the `daisho` db (will create if non-existing)
        daisho_db = connect.daisho
        if connect.database_names():
            print("Connection succesfully established")

    except pymongo.errors.ConnectionFailure as err:
        print("Failed to connect to {}".format(err))
        print("Check if the `mongod` service is running\n")
        sys.exit()
    return daisho_db


def add_data(data):
    """
    Add entries in the db
    """
    mongo_conn.daisho_db.subject.insert(data)
    # mongo_conn.daisho_db.table.insert(data)


def get_data(table, query):
    """
    Query the db and return data
    """
    return mongo_conn.daisho_db.table.find_one(query)


if __name__ == "__main__":
    mongo_conn()

