from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from .user import user_create
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

sign = Blueprint('sign_up', __name__, url_prefix='/auth')
uri = "mongodb://localhost:27017"
client = MongoClient(host = 'localhost', port = 27017, connect = True)
db = client.account#db 이름
coll = db.id#db의 collection 이름 테이블 같은 거

@sign.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = user_create()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)