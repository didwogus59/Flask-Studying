from web_project import create_app
#from web_project.chatting.test import socketio
from web_project.chatting.socket_test import socketio

if __name__ == '__main__':
    app = create_app()
    
    socketio.run(app)
    #app.run()
    

'''
conda activate FLASK
python run.py

$env:FLASK_APP = "web_project"
$env:FLASK_DEBUG="true"
flask run --host=0.0.0.0
'''
