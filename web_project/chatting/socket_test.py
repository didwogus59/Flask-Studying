from flask_socketio import emit, send
from flask_socketio import SocketIO 
from flask import Blueprint, render_template, request, session

web_socket = Blueprint("socket",__name__,url_prefix= '/socket')
#socketio = SocketIO(logger=True,engineio_logger=True)
socketio = SocketIO()

users = {}

@web_socket.route('/chat', methods = ['GET','POST',])
def chatting():
    return render_template("chatting/chat.html")

@socketio.on("connect")
def handle_connect():
    print("Client connected!")
    
@socketio.on("disconnect")
def handle_disconnect():
    session.clear()


@socketio.on("user_join")
def handle_user_join(username="default name"):
    session.clear()
    print(f"User {username} joined!")
    if username is not users:
        users[username] = username
        session['username'] = username

@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = session['username']
    emit("chat", {"message": message, "username": username}, broadcast=True)

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