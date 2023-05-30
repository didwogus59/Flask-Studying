from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from bson.objectid import ObjectId
from .form import mongo_form
mongo = Blueprint('mongo',__name__,url_prefix='/mongo')

uri = "mongodb://localhost:27017"
client = MongoClient(host = 'localhost', port = 27017, connect = True)
db = client.account#db 이름
coll = db.test#db의 collection 이름 테이블 같은 거
        
@mongo.route('/test',methods = ['GET','POST',])
def db_see():
    results = coll.find()#collection의 doccument 전부 찾기 doccument 는 sql의 row 같은 거 즉 데이터 하나
    #data = 
    #results.close()
    #client.close()
    return render_template('db/mongo.html', data = results)

@mongo.route('/test2',methods = ['GET','POST'])
def insert_page():
    if request.method == 'POST':
        data = request.form['data']
        content = request.form['content']
        document = {"name" : data, "content" : content}
        coll.insert_one(document)
        return redirect(url_for('mongo.db_see'))
    form = mongo_form()
    return render_template('db/db_insert.html', form = form)

@mongo.route('/test3/<id>')
def data_detail(id):
    data = coll.find_one({"_id":ObjectId(id)})#_id is objectid라는 타입이라 그냥 문자열로 찾으면 안 찾아진다
    return render_template('db/detail.html',data = data)

@mongo.route('/test4')
def data_delete():
    return redirect(url_for('mongo.db_see'))


@mongo.route('/test1',methods = ['GET','POST',])
def db_test1():
    db_list = client.list_databases()
    for item in db_list:
        print(item)
    print('\n')

    db_name = 'local'
    db = client.get_database(db_name)
    print(db)
    print('\n')

    for item in db.list_collection_names():
        print(item)
    print('\n')

    for item in db.list_collections():
        print(item)
    print('\n')

    coll_name = 'data'
    coll = db.get_collection(coll_name)
    print(coll)
    data = coll.find()
    print(data)
    print(data[0]['id'])
    print(type(data[0]['_id']))

    return '1'
    #client.close()
    return client.list_databases()
    #return render_template('mongo.html', data = results)