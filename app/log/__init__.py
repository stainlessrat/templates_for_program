import json
from logging.config import dictConfig
from pathlib import Path


def config_log(filename: str):
    log_config = Path(__file__).resolve().parent / filename
    dictConfig(json.load(open(log_config)))
