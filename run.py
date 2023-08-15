from web_project import create_app
if __name__ == '__main__':
    app = create_app()
    app.run(port = 8000, debug = True)

'''
conda deactivate
conda activate project_pybo
$env:FLASK_APP = "web_project"
$env:FLASK_DEBUG="true"
flask run --host=0.0.0.0
Flask-SocketIO==4.3.1
python-engineio==3.13.2
python-socketio==4.6.0
Flask==2.0.3
Werkzeug==2.0.3
"'''
