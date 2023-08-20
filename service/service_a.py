from nameko.events import EventDispatcher
from nameko.rpc import rpc


class ServiceA:
    """Event dispatching service."""

    name = "service_a"

    dispatch = EventDispatcher()

    @rpc
    def post_message(self, payload):
        self.dispatch("post_message", payload)

    @rpc
    def get_message(self, queue_name):
        self.dispatch("get_message", queue_name)
