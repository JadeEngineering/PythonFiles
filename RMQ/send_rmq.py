#!/usr/bin/env python3

"""
The simplest way to send via RMQ
"""

import pika
import pika.exceptions


def simple_sender(message: str = "Hello Rabbitmq",
                  host_name: str = "localhost",
                  queue_name: str = "hello",
                  routing_key: str = 'hello') -> bool:
    """

    :param message: Text to send
    :param host_name: Machine that runs the rabbitmq-server
    :param queue_name: RMQ-Queue to use
    :param routing_key: Routing key to use
    :return: Returning a True in case of a successful transmission, otherwise a False
    """

    send_complete = False
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host_name))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    try:
        channel.basic_publish(exchange='', routing_key=routing_key, body=message)
        send_complete = True

        print(" [x] Sent " + str(message))

    except pika.exceptions.ConnectionClosedByBroker:
        send_complete = False

    connection.close()

    return send_complete


if __name__ == "__main__":
    if simple_sender():
        print("Transmission successful")
    else:
        print("Transmission not successful")
