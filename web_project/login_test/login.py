from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from .user import login_form, coll

user_login = Blueprint("user_login", __name__, url_prefix="/login/user")


@user_login.route('/test1/', methods=('GET', 'POST'))
def login_test():
    form = login_form()
    if request.method == 'POST' and form.validate_on_submit():
        user = coll.find_one({"name":(form.name.data)})
        if not user:
            flash("id incorrect")
            return render_template('login/login.html', form=form)
        else:
            hash = generate_password_hash(user['content'])
            if not check_password_hash(hash, form.password.data):
                flash("password incorrect")
                return render_template('login/login.html', form=form)
            else:
                session.clear()
                session['user_id'] = user['name']
                return redirect(url_for('main.main_page'))
    return render_template('login/login.html', form=form)
#{{ form.csrf_token }} {% include "form_errors.html" %}#