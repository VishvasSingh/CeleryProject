from flask import Flask
from celery import Celery
from trigger_task import celery_trigger
from http import HTTPStatus

app = Flask(__name__)
celery_app = Celery('tasks')
celery_app.config_from_object('celery_config')


@app.route("/trigger_celery_task")
def call_celery():
    celery_trigger()
    return [], HTTPStatus.OK


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)