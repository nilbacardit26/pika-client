import pika


class RabbitmqConnection:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')

    def publish_message(self, message):
        self.channel.basic_publish(exchange='',
                                   routing_key='hello',
                                   body=message)
        print(f" [x] Sent {message}")

    def __exit__(self, *exc):
        print('Closing Connection')
        self.connection.close()


class Payload:
    def __init__(payload):
        self.payload = payload

    @property
    def title(self):


if __name__ == '__main__':
    connection = RabbitmqConnection()
    connection.publish_message('https://www.spotify.com')
