from flask import Blueprint, render_template, request, jsonify
from flask_socketio import SocketIO, send
web_socket = Blueprint("socket",__name__,url_prefix= '/socket')

count = 0
@web_socket.route('/chat',methods=('GET',))
def chatting():
    return render_template("chatting/web_socket.html")

socketio = SocketIO(logger=True,engineio_logger=True)


@socketio.on("message")
def request(message) :
    print("message :",message)
    to_client = dict()
    if message == 'new connect':
        to_client['message'] = "new client!"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    send(to_client,broadcast = True)