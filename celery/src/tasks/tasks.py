from celery import Celery

app = Celery('test', broker='amqp://rabbitmq//', backend='db+mysql://joey:chandler@mysql/backend-test')


@app.task
def add(x, y):
    return x + y