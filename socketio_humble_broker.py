from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import logging

logger = logging.getLogger(__name__)

import eventlet
import socketio

sio = socketio.Server()

app = socketio.WSGIApp(sio)

argparser = ArgumentParser(
    description='Start the socket.io-humber-broker server.',
    formatter_class=ArgumentDefaultsHelpFormatter,
)
argparser.add_argument(
    '--host',
    default='0.0.0.0',
    help='Host to listen to.',
)

argparser.add_argument(
    '--port',
    default=5000,
    type=int,
    help='Port to listen to.',
)

@sio.event
def connect(sid, environ):
    logger.info(f'new client sid:{sid} environ:{environ}')

@sio.event
def disconnect(sid):
    logger.info(f'client {sid} disconnected')

@sio.event
def broadcast(sid, data):
    sio.emit('broadcast', data, skip_sid=sid)

@sio.event
def subscribe(sid, room):
    sio.enter_room(sid, room)

@sio.event
def unsubscribe(sid, room):
    sio.leave_room(sid, room)

@sio.event
def publish(sid, room, data):
    sio.emit('data', (room, data), to=room)

def run(args=None):
    if not args:
        args = argparser.parse_args()

    eventlet.wsgi.server(eventlet.listen((args.host, args.port)), app)

if __name__ == '__main__':
    run()
