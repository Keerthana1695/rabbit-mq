from flask import Flask, request
import pika

app = Flask(__name__)

@app.route('/send')
def send():
    msg = request.args.get('msg', 'Hello from Flask!')
    
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))  # 'rabbitmq' = service name in OpenShift
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')
    channel.basic_publish(exchange='', routing_key='test_queue', body=msg)
    connection.close()
    
    return f"✅ Message sent: {msg}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # OpenShift expects port 8080
