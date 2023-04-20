from flask import Blueprint, render_template, request

form_test = Blueprint("form_test",__name__,url_prefix= '/test')

@form_test.route('/form',methods=('POST','GET',))
def test_form():
    data = request.form['data']
    password = request.form['password']
    print(data)
    print(password)
    return "data: " + data  + "\n password : " + password
