from nameko.events import event_handler
from nameko.rpc import rpc

class ServiceB:
    """ Event listening service. """
    name = __name__

    @event_handler("service_a", "event_type")
    def handle_event(self, payload):
        r = f"service b received: {payload}"
        print(r)
        return r
        