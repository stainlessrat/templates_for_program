import logging

from fastapi import BackgroundTasks, FastAPI, status

from .core import log, schemas
from .service import simple

log.config_log('app/settings/web.json')
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post('/', status_code=status.HTTP_200_OK)
async def webhook(webhook: schemas.Webhook, background_task: BackgroundTasks):
    _logger = logging.LoggerAdapter(logger, {'some_user_key': 'test'})
    background_task.add_task(main, _logger, webhook)


def main(_logger: logging.LoggerAdapter, webhook: schemas.Webhook):
    simple.my_func_background_task(_logger, webhook)


@app.get('/api/v1/get')
async def simple_api():
    _logger = logging.LoggerAdapter(logger, {'some_user_key': 'test'})
    result = simple.my_func_simple(_logger)
    return result


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
async def healthcheck():
    return {'msg': 'ok'}
