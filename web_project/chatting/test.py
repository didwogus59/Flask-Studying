from flask import Blueprint, render_template
from flask_socketio import SocketIO, send
web_socket = Blueprint("socket",__name__,url_prefix= '/socket')

@web_socket.route('/chat',methods=('GET',))
def chatting():
    return render_template("chatting/test.html")

socketio = SocketIO(engineio_logger=True, logger=True)


@socketio.on("message")
def request(message):
    print("message : "+ message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = "새로운 유저가 난입하였다!!"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
    send(to_client, broadcast=True)