from flask import Blueprint, render_template, session, g, url_for
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from werkzeug.utils import redirect
main = Blueprint('main',__name__,url_prefix='/')

uri = "mongodb://localhost:27017"
client = MongoClient(host = 'localhost', port = 27017, connect = True)
db = client.account#db 이름
coll = db.id#db의 collection 이름 테이블 같은 거

@main.route('/')
def main_page():
    return render_template('main.html')

@main.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@main.before_app_request
def load_logged_in_user():
    user_id = session.get('name')
    if user_id is None:
        g.user = None
    else:
        data = coll.find_one({"_id":ObjectId(user_id)})
        g.user = data

@main.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.main_page'))

