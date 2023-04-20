from flask import Blueprint, render_template, request, jsonify

send_var = Blueprint("send_var",__name__,url_prefix= '/var')

@send_var.route('/send/<var>',methods=('POST','GET',))
def chatting(var):
    return render_template("argument.html", var = var)