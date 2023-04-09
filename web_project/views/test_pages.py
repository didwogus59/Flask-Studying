from flask import Blueprint

test = Blueprint("test",__name__,url_prefix= '/test')

@test.route('/1/<var>',methods=('GET',))
def test_var(var):
    return "test var: " + var