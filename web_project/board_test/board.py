from flask import Blueprint, url_for, render_template, flash, request, session
from bson.objectid import ObjectId
from werkzeug.utils import redirect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from .form import board_form
uri = "mongodb://localhost:27017"
client = MongoClient(host = 'localhost', port = 27017, connect = True)
db = client.account#db 이름
post_board = db.board#db의 collection 이름 테이블 같은 거
id = db.id
board = Blueprint('board', __name__, url_prefix='/board')

@board.route('/list',methods = ['GET','POST',])
def db_see():
    results = post_board.find()
    return render_template('board_test/board.html', data = results)

@board.route('/post/new',methods = ['GET','POST',])
def post_insert():
    user_id = session.get('name')
    if user_id is None:
        return redirect(url_for('board.db_see'))
    else:
        form = board_form()
        if request.method == 'POST' and form.validate_on_submit():
            data = id.find_one({"_id":ObjectId(user_id)})
            title = form.title.data
            content = form.content.data
            document = {"name":data['name'], "title":title, "content":content}
            post_board.insert_one(document)
            return redirect(url_for('board.db_see'))
        else:
            return render_template('board_test/post.html',form = form)
        
@board.route('/post/detail',methods = ['POST','GET',])
def post_detail():
    return "1"

@board.route('/post/delete',methods = ['POST','GET',])
def post_delete():
    return "1"
