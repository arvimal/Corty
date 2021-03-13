#!/usr/bin/env python3

import graphene

class Query(graphene.ObjectType):
    query = graphene.String(name = graphene.String())

    @staticmethod
    def resolve_query(parent, info, name):
        return("Hello {}".format(name))