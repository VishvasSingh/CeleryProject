import logging as logger
from tasks import add, subtract


def celery_trigger():
    add.delay(x=3, y=4)
    subtract.delay(x=4, y=3)
    logger.info("Triggered celery tasks")
