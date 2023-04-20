from flask import Blueprint, render_template, request, jsonify

chat_client1 = Blueprint("chat",__name__,url_prefix= '/chat')

@chat_client1.route('/user',methods=('POST','GET',))
def chatting():
    print("syncing")
    return render_template("chat.html")