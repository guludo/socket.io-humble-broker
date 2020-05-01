#######################
socket.io-humble-broker
#######################


This is a very very simple socket.io server to act as a message broker with
support to the publish/subscribe pattern using socket.io rooms.

Usage
=====

The server can be started by either using ``socket.io-humble-broker`` or
``python -m socketio socketio_humble_broker``.

See below the output of ``socket.io-humble-broker --help``:

::
    usage: socket.io-humble-broker [-h] [--host HOST] [--port PORT]

    Start the socket.io-humber-broker server.

    optional arguments:
      -h, --help   show this help message and exit
      --host HOST  Host to listen to. (default: 0.0.0.0)
      --port PORT  Port to listen to. (default: 5000)


Socket.io events:
=================

Events emitted by the client
----------------------------

A client can communicate with the broker by emitting the following events:

``subscribe``
    Arguments: ``room``

    Subscribe to a socket.io room.

``publish``
    Arguments: ``room``, ``msg``

    Publish ``msg`` to ``room``. All subscribed clients will receive an event
    of type ``data``.

``broadcast``
    Arguments: ``msg``

    Broadcast ``msg``. An event of type ``broadcast`` will be emitted to all
    connected clients (except the sender).


Events received by the client
-----------------------------

The broker emits the following types of events to connected clients:

``data``
    Arguments: ``room``, ``msg``

    This event is emitted to the client when a message when the broker receives
    a message in one room the client has subscribed to.

``broadcast``
    Arguments: ``msg``

    The event is emitted to the client whenever a ``broadcast`` message from
    another client is received by the broker.


Installation
============

.. TODO: uncomment this when made available on pypi.org
.. Using ``pip``
.. -------------

.. .. code:: bash

..    pip install socket.io-humble-broker

From source
-----------

If you have ``pip`` available in your system, then the recommended way to
install from source is doing:

.. code:: bash

    # From the source root
    pip install .

Alternatively, you can also call ``setup.py`` directly, but remember that it
*does not provide an "uninstall" command* (this form is useful for OS
distribution packagers):

.. code:: bash

    python setup.py install
