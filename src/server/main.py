#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
def hello():
    return("Hello, I am FastAPI")
