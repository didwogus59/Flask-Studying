from flask import Flask
from flask_socketio import SocketIO

socketio1 = SocketIO()

def create_app(port = 8000, debug = True):


    app = Flask(__name__)
    app.debug = debug
    socketio1.init_app(app)

    from .views import main_pages, chat_client
    app.register_blueprint(main_pages.main)
    app.register_blueprint(chat_client.chat_client1)
    
    from .test import get_test, post_test, form_test, json_test, argument
    app.register_blueprint(get_test.get_test)
    app.register_blueprint(post_test.post_test)
    app.register_blueprint(form_test.form_test)
    app.register_blueprint(json_test.json_test1)
    app.register_blueprint(argument.send_var)

    
    return app
    
#app.run(port = 8000, debug = False)

#app = create_app()
#app.run(port = 8000, debug = False)
'''
conda deactivate
conda activate project_pybo
$env:FLASK_APP = "web_project"
$env:FLASK_DEBUG="true"
flask run --host=0.0.0.0
"'''