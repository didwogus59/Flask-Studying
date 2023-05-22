from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect

db_name = 'local'
coll_name = 'data'
login = Blueprint('login',__name__,url_prefix='/login')
uri = "mongodb://localhost:27017"

@login.route('/test1', methods = ['GET','POST'])
def login_page():
    return render_template('login.html')

@login.route('/test2',methods = ['GET','POST',])
def db_test2():
    id = request.form['id']
    pwd = request.form['pwd']
    client = MongoClient(host = 'localhost', port = 27017, connect = True)
    db = client.get_database(db_name)
    coll = db.get_collection(coll_name)
    data = coll.find_one({'id':id})

    if data is None:
        flash("id don't exist")
        return render_template('login.html')
    if(data['pwd'] != pwd):
        flash("wrong pwd")
        return render_template('login.html')
    return render_template('login.html')
