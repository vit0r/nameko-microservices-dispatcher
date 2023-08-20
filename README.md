# Nameko /o/

```console
code .
docker run -d -p 15672:15672 -p 5672:5672 rabbitmq:3-management
python3 -m pip install -r requirements.txt -U # without virtualenv activated
cd service
nameko run service_a service_b --broker amqp://guest:guest@localhost
# on vscode press F5 to run flask
```
