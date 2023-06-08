from flask import Blueprint, render_template, request, jsonify, url_for
from werkzeug.utils import redirect
json_test = Blueprint("json_test",__name__,url_prefix= '/json')

@json_test.route('/test',methods=('POST','GET',))
def test_json():
    if request.method == "POST":
        form = request.form
        title = form['title']
        content = form['content']
        json = jsonify({'title':title, 'content':content})
        print(json)
        return json
    else:
        return render_template("post_get_test/form_get.html")
