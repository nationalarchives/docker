import multiprocessing
import os

cpu_cores = multiprocessing.cpu_count()
workers = int(os.environ.get("WORKERS", cpu_cores * 2 + 1))
worker_class = os.environ.get("WORKER_CLASS", "sync")
threads = int(os.environ.get("THREADS", "1"))
worker_connections = int(os.environ.get("WORKER_CONNECTIONS", "1000"))
max_requests = int(os.environ.get("MAX_REQUESTS", "10000"))
max_requests_jitter = int(os.environ.get("MAX_REQUESTS_JITTER", "1000"))
loglevel = os.environ.get("LOG_LEVEL", "warning").lower()
timeout = int(os.environ.get("TIMEOUT", "30"))
graceful_timeout = int(os.environ.get("GRACEFUL_TIMEOUT", "30"))
asgi_loop = "auto"  # Use uvloop if available
asgi_lifespan = "auto"  # Auto-detect lifespan support
keepalive = int(
    os.environ.get("KEEP_ALIVE", "65")
)  # Ensure this is larger than Traefik's keep-alive configuration (default 60s)
protocol = os.environ.get(
    "GUNICORN_PROTOCOL", "http"
)  # http or uwsgi (https://gunicorn.org/uwsgi/)
http_protocols = os.environ.get("HTTP_PROTOCOLS", "h1")  # h1, h2 or h2,h1
root_path = os.environ.get("ROOT_PATH", "")  # Used by ASGI applications
accesslog = "-"
bind = f"0.0.0.0:{os.environ.get('APPLICATION_PORT', '8080')}"
preload_app = os.environ.get("PRELOAD_APP", "false").lower() == "true"
capture_output = True
enable_stdio_inheritance = True

application_protocol = os.environ.get("APPLICATION_PROTOCOL", "https").lower()
if application_protocol not in ("http", "https"):
    raise ValueError(
        "APPLICATION_PROTOCOL must be either 'http' or 'https', "
        f"not {application_protocol!r}"
    )

if application_protocol == "https":
    keyfile = os.environ.get("SSL_KEY_FILE", "/home/app/ssl/server.key")
    certfile = os.environ.get("SSL_CERTIFICATE_FILE", "/home/app/ssl/server.crt")
    ca_certs = os.environ.get("SSL_CA_CERTIFICATES_FILE") or None
