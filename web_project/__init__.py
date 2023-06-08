from flask import Flask, session
from flask_socketio import SocketIO
import os
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta

socketio1 = SocketIO()

def create_app():
    app = Flask(__name__, template_folder= "templates")
    app.config.update(
    DEBUG=True
    )
    app.config.from_pyfile('../config.py')
    socketio1.init_app(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=1)

    from .views import main_pages
    app.register_blueprint(main_pages.main)

    from .test import argument
    app.register_blueprint(argument.send_var)

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

if __name__ == '__main__':
    app = create_app()
    app.run()

#app.run(port = 8000, debug = False)

#app = create_app()
#app.run(port = 8000, debug = False)
'''
conda deactivate
conda activate project_pybo
$env:FLASK_APP = "web_project"
$env:FLASK_DEBUG="true"
flask run
 --host=0.0.0.0
"'''