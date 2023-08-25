import functools

import flask


def json_response(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        body = flask.jsonify(result)
        status = 200
        headers = {}

        headers.update({"ContentType": "application/json"})
        return flask.make_response((body, status, headers))

    return wrapper
