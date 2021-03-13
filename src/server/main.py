#!/usr/bin/env python3

import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from schema import Query

app = FastAPI(
    title="Daisho API", description="Daisho GraphQL FastAPI interface", version="0.1"
)

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))


@app.get("/api")
def hello():
    return "Hello, I am FastAPI"
