#!/usr/bin/env python3

import graphene
from fastapi import FastAPI
from helpers import logger
from starlette.graphql import GraphQLApp

from .schema import Query

app = FastAPI(
    title="Corty API", description="Corty GraphQL FastAPI interface", version="0.1"
)

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))


@app.get("/api")
def hello():
    return "Hello, I am FastAPI"
