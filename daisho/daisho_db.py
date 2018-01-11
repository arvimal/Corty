#!/usr/bin/env python3

import pymongo

def mongo_conn():
    try:
        connection = pymongo.MongoClient()
        host, port = connection.address
        print("\nConnecting to {} on {}".format(host, port))
        print("Active DBs : {}".format(connection.database_names()))
    except pymongo.errors.ConnectionFailure as err:
        print("Failed to connect : {}".format(err))

if __name__ == "__main__":
    mongo_conn()

