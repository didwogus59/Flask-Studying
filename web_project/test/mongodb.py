from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Blueprint, render_template

mongo = Blueprint('mongo',__name__,url_prefix='/mongo')

@mongo.route('/test',methods = ['GET','POST',])
def db_test():
    uri = "mongodb://localhost:27017"
    client = MongoClient(host = 'localhost', port = 27017, connect = True)
    db = client.local#db 이름
    collection = db.data#db의 collection 이름 테이블 같은 거
    results = collection.find()#collection의 doccument 전부 찾기 doccument 는 sql의 row 같은 거 즉 데이터 하나
    #client.close()
    return render_template('mongo.html', data = results)

@mongo.route('/test1',methods = ['GET','POST',])
def db_test1():
    uri = "mongodb://localhost:27017"
    client = MongoClient(host = 'localhost', port = 27017, connect = True)
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
    print(data[0]['data'])

    return '1'
    #client.close()
    return client.list_databases()
    #return render_template('mongo.html', data = results)

