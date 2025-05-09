FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install flask pika

EXPOSE 8080

CMD ["python", "rabbit.py"]
