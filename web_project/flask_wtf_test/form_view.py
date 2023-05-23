from .form import test_form

from flask import Blueprint, render_template, request, url_for

form_testing = Blueprint("form_tests",__name__,url_prefix = '/form_testing')

@form_testing.route('/test1',methods = ['POST','GET',])
def view():
    form = test_form()
    return render_template("wtf_view.html",data = form)

@form_testing.route('/test2', methods = ['POST','GET',])
def send():
    form = test_form()
    return render_template('wtf_send.html', form = form)