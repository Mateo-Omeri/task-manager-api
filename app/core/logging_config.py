import logging
import sys


def configure_logging():
    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))

    app_logger = logging.getLogger("app")
    app_logger.setLevel(logging.DEBUG)
    app_logger.addHandler(console_handler)
    app_logger.propagate = False

    uvicorn_loggers = ["uvicorn", "uvicorn.error", "uvicorn.access"]
    for name in uvicorn_loggers:
        logger = logging.getLogger(name)
        logger.handlers = [console_handler]
        logger.setLevel(logging.INFO)

    app_logger.info("Logging configured successfully.")
