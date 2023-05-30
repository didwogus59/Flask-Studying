from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField
from wtforms.validators import DataRequired
class mongo_form(FlaskForm):
    name = StringField("이름",[validators.length(min = 1, max = 6)])
    content = TextAreaField("내용", validators=[DataRequired()])