from .form import test_form

from flask import Blueprint, render_template, request, url_for

form_testing = Blueprint("form_tests",__name__,url_prefix = '/form_wtf')

@form_testing.route('/test',methods = ['POST','GET',])
def test():
    form = test_form()
    if request.method == "POST":
        return render_template("wtf_test/wtf_view.html",data = form)
    else:
        return render_template('wtf_test/wtf_send.html', form = form)