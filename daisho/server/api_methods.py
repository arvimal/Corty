from fastapi import FastAPI, Query

api = FastAPI()

@api.get("/")
def get_index():
    return("Welcome to Daisho")

@api.get("/help"):
def get_help():
    """[summary]
    """
    pass
