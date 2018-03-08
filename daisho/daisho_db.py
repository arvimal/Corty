#!/usr/bin/env python3

# Copyright (C) 2016 Vimal A.R <arvimal@yahoo.in>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import pymongo
import sys

HOST = "localhost"
PORT = "27017"


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


if __name__ == "__main__":
    mongo_conn()
