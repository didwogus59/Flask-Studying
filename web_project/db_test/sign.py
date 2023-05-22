from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
bp = Blueprint('sign',__name__,url_prefix='/sign')

@bp.route('/up',methods = ['GET','POST',])
def db_see():
    uri = "mongodb://localhost:27017"
    client = MongoClient(host = 'localhost', port = 27017, connect = True)
    db = client.local#db 이름
    collection = db.data#db의 collection 이름 테이블 같은 거
    results = collection.find({"data":"1234"})#collection의 doccument 전부 찾기 doccument 는 sql의 row 같은 거 즉 데이터 하나
    #client.close()
    return render_template('mongo.html', data = results)

@bp.route('/test',methods = ['GET','POST',])
def sign_up():
    return 1