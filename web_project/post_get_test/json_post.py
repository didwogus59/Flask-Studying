from flask import Blueprint, render_template, request, jsonify

json_test1 = Blueprint("json_test1",__name__,url_prefix= '/test')

@json_test1.route('/json',methods=('POST','GET',))
def test_form():
    if(request.is_json) :
        data = request.get_json()
        ans = "data send success " + data['data'] + " and " + data['password'] 
        return ans
    else :
        return "not json"
