
from flask import Flask, render_template
from flask_socketio import SocketIO, send
#from ...web_project import socket_io1
from .. import socket_io1

@socket_io1.on("message")
def request(message):
    print("message : " + message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = "welcome tester"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    send(to_client, broadcast = True)