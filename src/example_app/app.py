import flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


def setup_sentry(config):
    if not config.enabled:
        return

    sentry_sdk.init(
        dsn=config.dsn,
        integrations=[
            LoggingIntegration(level=config.breadcrumb_level, event_level=config.level),
            FlaskIntegration(),
        ],
        attach_stacktrace=True,
        environment=config.environment,
        server_name=config.service_name,
        traces_sample_rate=1.0,
    )


def create_app(config):
    from example_app import routes

    app_ = flask.Flask(__name__)

    for method, path, view in routes:
        endpoint = ".".join([view.__module__, view.__name__])
        decorator = app_.route(path, methods=[method], endpoint=endpoint)
        decorator(view)

    return app_
