from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from .form import user_create
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

sign = Blueprint('sign_up', __name__, url_prefix='/auth')
uri = "mongodb://localhost:27017"
client = MongoClient(host = 'localhost', port = 27017, connect = True)
db = client.account#db 이름
coll = db.id#db의 collection 이름 테이블 같은 거

@sign.route('/signup/', methods=('GET', 'POST'))
def sign_up():
    form = user_create()
    if request.method == 'POST' and form.validate_on_submit():
        user = coll.find_one({'name':(form.name.data)})
        if not user:
            name = form.name.data
            password = form.password.data
            email = form.email.data
            document = {"name":name, "password": generate_password_hash(password), "email" : email}
            coll.insert_one(document)
            return redirect(url_for('user_login.login_test'))
        else:
            flash('name duplication')
    return render_template('login/sign_up.html', form=form)