from flask import Blueprint, render_template,jsonify
import os
post_test = Blueprint("post_test",__name__,url_prefix= '/test')

@post_test.route('/post/<var>',methods=('POST','GET',))
def test_post(var):
    return "test get: " + var

@post_test.route('/post/form',methods=('POST','GET',))
def test_post1():
    return render_template("form.html")

@post_test.route('/post/json/<data>/',methods = ('POST', 'GET',))
def test_post2(data):
    return jsonify({"data":data})