#!/usr/bin/env python3

from fastapi import FastAPI
from src.helpers import logger


app = FastAPI(
    title="Corty API", description="Corty GraphQL FastAPI interface", version="0.1"
)

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))


@app.get("/api")
def hello():
    return "Hello, I am FastAPI"
