from flask import Flask
import random
def create_app():
    app = Flask(__name__)

    from .views import main_pages, test_pages
    app.register_blueprint(main_pages.main)
    app.register_blueprint(test_pages.test)
  
    @app.route('/var/<id>')
    def var_test(id):
        return "test var" + id
    
    return app
#app.run(port = 8000, debug = False)


'''
$env:FLASK_APP = "web_project"
$env:FLASK_DEBUG="true"
"'''