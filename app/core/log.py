import gzip
import json
import logging
import os
from datetime import datetime
from logging.config import dictConfig
from logging.handlers import RotatingFileHandler
from pathlib import Path


def config_log(filepath: str):
    dictConfig(json.load(Path(filepath).open()))


class SomeKeyFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if not hasattr(record, 'some_key'):
            setattr(record, 'some_key', '')
        return True


class FilterHealthCheck(logging.Filter):
    def filter(self, record) -> bool:
        return '/healthcheck' not in record.args  # type: ignore


class GzRotatingFileHandler(RotatingFileHandler):
    def namer(self, name):
        return f'{name}_{datetime.now()}.gz'

    def rotator(self, source, dest):
        with open(source, 'rb') as sf:
            data = sf.read()
            compressed = gzip.compress(data, 9)
            with gzip.GzipFile(dest, 'wb') as df:
                df.write(compressed)
        os.remove(source)
