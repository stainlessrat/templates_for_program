import logging

from app.core import schemas


def my_func_background_task(logger: logging.LoggerAdapter, webhook: schemas.Webhook):
    logger.info(my_func_background_task.__name__)
    logger.debug(webhook)
    logger.info('OK')


def my_func_simple(logger: logging.LoggerAdapter):
    logger.info(my_func_simple.__name__)
    logger.debug('Test')
    logger.info('OK')
    return {'msg': 'ok'}
