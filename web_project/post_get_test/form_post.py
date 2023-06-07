from flask import Blueprint, render_template, request

form_test = Blueprint("form_test",__name__,url_prefix= '/test')

@form_test.route('/form',methods=('POST','GET',))
def test_form():
    if request.method == "POST":
        data = request.form['title']
        password = request.form['content']
    else:
        return render_template()
