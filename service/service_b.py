from nameko.events import event_handler
from nameko.rpc import rpc

class ServiceB:
    """ Event listening service. """
    name = __name__

    @event_handler("service_a", "post_message")
    def post_message(self, payload):
        r = f"service b received: {payload}"
        print(r)
        return r
    
    @event_handler("service_a", "get_message")
    def get_message(self, queue_name):
        message = 'test message'
        r = f"service b getter: {message}"
        print(r)
        return r
        