import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

def callback(ch, method, properties, body):
    print(f'[*] Received:\n{body}')

channel = connection.channel()
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('[*] Waiting for messages.')
channel.start_consuming()