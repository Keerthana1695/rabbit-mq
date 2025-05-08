local Rabbit MQ test 

run app.py

send message through http://localhost:5000/send?msg={message}

read the message here -http://localhost:5000/read

to check if the message is in queue in rabbit mq , send the message and before reading go to rabbit mq UI-http://localhost:15672/#/queues/%2F/demo_queue{guest , guest}, go to queue and streams -get message -you will find the text we send if we click the get message button
