# Run

`docker run -d --hostname my-rabbit --name some-rabbit1 -p 15672:15672 -p 5672:5672 rabbitmq:3-management`

`nameko run service_a service_b --broker amqp://guest:guest@localhost`
