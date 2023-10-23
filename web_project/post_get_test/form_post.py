from flask import Blueprint, render_template, request
from ..chatting.extension import socketio
form_test = Blueprint("form_test",__name__,url_prefix= '/form')

@form_test.route('/test',methods=('POST','GET',))
def test_form():
    if request.method == "POST":
        form = request.form
        data = form['title']
        content = form['content']
        return render_template("post_get_test/form_post.html",form = form)
    else:
        return render_template("post_get_test/form_get.html")