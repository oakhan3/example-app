from flask import request

from example_app.decorators import json_response


@json_response
def create():
    payload = request.get_json()
    return {"key": str(payload)}


@json_response
def read(entity_id):
    return {"key": entity_id}


@json_response
def read_all():
    return {"key": "value"}


@json_response
def update():
    payload = request.get_json()
    return {"key": str(payload)}


@json_response
def delete():
    return {"key": "value"}


def raise_error():
    raise Exception("OMG HELP")
