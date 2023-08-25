from configly import Config

from example_app import create_app, setup_sentry

config = Config.from_yaml("config.yml")

app = create_app(config)

if __name__ == "__main__":
    setup_sentry(config.sentry)

    app.run()
