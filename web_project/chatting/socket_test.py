from flask import Blueprint, render_template, request
from flask_socketio import emit, send
from .extension import socketio
web_socket = Blueprint("socket",__name__,url_prefix= '/socket')

users = {}

@web_socket.route('/chat', methods = ['GET','POST',])
def chatting():
    return render_template("chatting/chat.html")
    

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

@socketio.on("user_join")
def handle_user_join(username = "default"):
    print(f"User {username} joined!")
    users[username] = request.sid

@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)