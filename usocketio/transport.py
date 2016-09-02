"""SocketIO transport."""

import logging
import ujson as json

from .protocol import *

LOGGER = logging.getLogger(__name__)


class SocketIO:
    """SocketIO transport."""

    def __init__(self, websocket):
        self.websocket = websocket
        self._handlers = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def close(self):
        self.websocket.close()

    def run_forever(self):
        """Main loop for SocketIO."""
        LOGGER.debug("Entering event loop")
        while True:
            # FIXME: need a timeout so that we can send ping messages
            packet_type, data = self._recv()
            self._handle_packet(packet_type, data)

    def _handle_packet(self, packet_type, data):
        if packet_type == PACKET_MESSAGE:
            message_type, data = decode_packet(data)
            self._handle_message(message_type, data)
        else:
            print("Unhandled packet", packet_type, data)

    def _handle_message(self, message_type, data):
        if message_type == MESSAGE_EVENT:
            event, data = json.loads(data)
            LOGGER.debug("Handling event '%s'", event)

            for handler in self._handlers.get(event, []):
                LOGGER.debug("Calling handler %s for event '%s'",
                             handler, event)
                handler(self, data)
        else:
            print("Unhandled message type", message_type, data)

    def _send_packet(self, packet_type, data=''):
        self.websocket.send('{}{}'.format(packet_type, data))

    def _recv(self):
        return decode_packet(self.websocket.recv())

    def on(self, event):
        """Register an event handler with the socket."""

        def inner(func):
            LOGGER.debug("Registered %s to handle %s", func, event)
            self._handlers.setdefault(event, []).append(func)

        return inner