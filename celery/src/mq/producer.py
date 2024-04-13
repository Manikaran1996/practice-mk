import pika
import time
import random
from . import HOST


def print_log(*args):
    print("Message consumed: {}".format(args))


if __name__ == '__main__':
    cnx = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=5672))
    channel = cnx.channel()
    channel.exchange_declare('logs_exchange')
    queue = channel.queue_declare('logs')
    queue_name = queue.method.queue
    channel.queue_bind(queue=queue_name, exchange='logs_exchange', routing_key='test')
    print('Starting to produce...')
    while True:
        rand_num = random.randint(0, 100)
        print('Producing: {}'.format(rand_num))
        channel.basic_publish(exchange='logs_exchange', routing_key='test',
                              body='Number generated: {}'.format(rand_num).encode('utf-8'))

        time.sleep(1)