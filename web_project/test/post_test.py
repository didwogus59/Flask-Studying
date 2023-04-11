from flask import Blueprint

post_test = Blueprint("post_test",__name__,url_prefix= '/test')

@post_test.route('/post/<var>',methods=('POST','GET',))
def test_post(var):
    print(var)
    return "test get: " + var

@post_test.route('/post/',methods=('POST','GET'))
def test_post1():
    return "test get: " + "10"