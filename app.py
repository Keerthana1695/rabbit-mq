from flask import Flask, request, jsonify
import pika

app = Flask(__name__)
QUEUE_NAME = 'demo_queue'
RABBITMQ_HOST = 'localhost'

def connect_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    return connection, channel

@app.route('/send', methods=['GET'])
def send_message():
    msg = request.args.get('msg', 'Hello from Flask!')
    connection, channel = connect_channel()
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=msg)
    connection.close()
    return jsonify({'status': 'sent', 'message': msg})

@app.route('/read', methods=['GET'])
def read_messages():
    connection, channel = connect_channel()
    messages = []
    while True:
        method_frame, _, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
        if method_frame:
            messages.append(body.decode())
        else:
            break
    connection.close()
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
