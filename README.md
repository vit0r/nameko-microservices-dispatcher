# Run
`$ docker run -d --hostname my-rabbit --name some-rabbit1 -p 15672:15672 -p 5672:5672 rabbitmq:3-management`

`$ cd nameko-microservices-dispatcher/`

`$ pipenv shell`

`$ pipenv update`


`$ cd service`

`$ nameko run service_a service_b --broker amqp://guest:guest@localhost`

`$ code.`

#### on vscode press F5 to run flask