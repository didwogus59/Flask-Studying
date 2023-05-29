from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from .user import login_form, coll

user_login = Blueprint("user_login", __name__, url_prefix="/login/user")


@user_login.route('/test1/', methods=('GET', 'POST'))
def login_test():
    form = login_form()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = coll.find_one({"name":(form.name.data)})
        hash = generate_password_hash(user['content'])
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(hash, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user['name']
            return redirect(url_for('main.main_page'))
        print(error)
    return render_template('login/login.html', form=form)

#{{ form.csrf_token }} {% include "form_errors.html" %}#