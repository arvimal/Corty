#!/usr/bin/env python3

"""
This module searching existing notes and tasks based on
patterns and regular expressions.
"""

import logging

from server import daisho_db

logger = logging.getLogger(__name__)


def get_data(table, query: str):
    """
    Query the db and return data
    """
    conn_query = daisho_db.mongo_conn()
    return conn_query.daisho_db.table.find_one(query)
