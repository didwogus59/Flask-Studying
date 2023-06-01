from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms.fields.html5 import EmailField
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

uri = "mongodb://localhost:27017"
client = MongoClient(host = 'localhost', port = 27017, connect = True)
db = client.account#db 이름
coll = db.id#db의 collection 이름 테이블 같은 거

class user_create(FlaskForm):
    name = StringField("아이디",[validators.length(min = 1, max = 13)])
    email = EmailField("이메일", validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호",[
        validators.DataRequired(),
        validators.EqualTo('password_confirm',message= 'passwords must be matched'),
    ])
    password_confirm = PasswordField('Repeat Password')
    #check = BooleanField('i checked', [validators.input_required()])


class login_form(FlaskForm):
    name = StringField('아이디', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])