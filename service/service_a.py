
from nameko.events import EventDispatcher
from nameko.rpc import rpc

class ServiceA:
    """ Event dispatching service. """
    name = __name__

    dispatch = EventDispatcher()

    @rpc
    def dispatching_method(self, payload):
        self.dispatch("event_type", payload)