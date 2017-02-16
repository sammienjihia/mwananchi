# import datetime
# from celery import Celery
# from celery import group
# from sendtext import receivedsms
#
# app = Celery('mwananchi', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
#
# @app.task
# def task_receivedsms():
#     values = receivedsms()
#     return values
#
# app.conf.update(
#     CELERYBEAT_SCHEDULE={
#         'multiply-each-10-seconds': {
#             'task': 'tasks.task_receivedsms',
#             'schedule': datetime.timedelta(seconds=10),
#             'args': (2, )
#         }
#     }
# )
#
#
#

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import timedelta
from sendtext import receivedsms

logger = get_task_logger(__name__)


@periodic_task(
    run_every=timedelta(seconds=7),
    name="task_receivedsms",
    ignore_result=True
)
def task_receivedsms():
    """
    Gets latest messages from Africa's talking API
    """
    receivedsms()
    logger.info("Checked the Africa's talking api")

