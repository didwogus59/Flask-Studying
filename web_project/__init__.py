from flask import Flask
import random
def create_app():
    app = Flask(__name__)

    from .views import main_pages
    from .test import get_test, post_test
    app.register_blueprint(main_pages.main)
    app.register_blueprint(get_test.get_test)
    app.register_blueprint(post_test.post_test)
    
    return app
#app.run(port = 8000, debug = False)


'''
$env:FLASK_APP = "web_project"
$env:FLASK_DEBUG="true"
"'''