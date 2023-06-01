from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired
class board_form(FlaskForm):
    name = StringField("writer")
    title = StringField("title",validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])