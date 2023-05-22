from flask import Blueprint

get_test = Blueprint("get_test",__name__,url_prefix= '/test')

@get_test.route('/get/<var>',methods=('GET',))
def test_get(var):
    return "test get: " + var