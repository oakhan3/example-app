import os

host = ""
port = os.environ.get("APP_PORT", 5000)
bind = f"{host}:{port}"
workers = int(os.environ.get("WORKER_COUNT", 5))

max_requests = 500
max_requests_jitter = 50

timeout = 300
graceful_timeout = 300

accesslog = "-"
errorlog = "-"
log_file = "-"

preload_app = "RELOAD" not in os.environ
