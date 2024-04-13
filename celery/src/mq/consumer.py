import pika
from mq import HOST


def print_log(*args):
    print("Message consumed: {}".format(args))


if __name__ == '__main__':
    cnx = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=5672))
    channel = cnx.channel()
    channel.exchange_declare('logs_exchange')
    queue = channel.queue_declare('logs')
    queue_name = queue.method.queue
    channel.queue_bind(queue=queue_name, exchange='logs_exchange')
    channel.basic_consume(queue=queue_name, on_message_callback=print_log, auto_ack=True)
    print('Starting to consume...')
    channel.start_consuming()
