import logging as logger
from celery import Celery

celery_app = Celery('tasks')
celery_app.config_from_object('celery_config')


@celery_app.task
def add(x, y):
    logger.info(f'High priority Celery task has output {x+y}')


@celery_app.task
def subtract(x, y):
    logger.info(f'Low priority Celery task has output {x-y}')