import os

host = ""
port = os.environ.get("APP_PORT", 5000)
bind = f"{host}:{port}"
