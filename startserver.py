import signal
import os

from jedi_language_server.cli import cli


def signal_handler(signum, frame):
    os._exit(1)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
cli()
