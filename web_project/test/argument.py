from flask import Blueprint, render_template, request, jsonify

send_var = Blueprint("send_var",__name__,url_prefix= '/var')

count = 0
@send_var.route('/send/<int:var>',methods=('POST','GET',))
def chatting(var):
    global count
    count = (int(var) + count) % 10000000
    return render_template("argument.html", var = count)