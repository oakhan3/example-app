import pytest
from configly import Config

from example_app import create_app


@pytest.fixture()
def app():
    config = Config.from_yaml("config.yml")

    app = create_app(config)
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
