from flask import Flask, session
import os
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
#from .chatting.test import *
from .chatting.socket_test import *

from dotenv import load_dotenv
load_dotenv()

def create_app():
    
    app = Flask(__name__, template_folder= "templates")
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=1)
    app.config['DEBUG'] = os.environ.get('DEBUG')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') 
    socketio.init_app(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    
    app.register_blueprint(web_socket)
    
    from .views import main_pages
    app.register_blueprint(main_pages.main)

    from .test import argument
    app.register_blueprint(argument.send_var)

    from .post_get_test import form_post, json_post
    app.register_blueprint(form_post.form_test)
    app.register_blueprint(json_post.json_test)

    from .db_test import mongodb
    app.register_blueprint(mongodb.mongo)
    
    from .flask_wtf_test import form_view
    app.register_blueprint(form_view.form_testing)
    
    from .login_test import login, sign
    app.register_blueprint(login.user_login)
    app.register_blueprint(sign.sign)

    from .board_test import board
    app.register_blueprint(board.board)
    return app