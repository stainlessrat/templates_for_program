import gzip
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler


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
