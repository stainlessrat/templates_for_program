import logging

from fastapi import FastAPI, status

from app import log

log.config_log('web.json')
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post('/')
async def main():
    _logger = logging.LoggerAdapter(logger, {'some_user_key': 'test'})
    _logger.debug('Call main function')
    _logger.info('Main function finish')
    return {'msg': 'ok'}


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
async def healthcheck():
    return {'msg': 'ok'}
