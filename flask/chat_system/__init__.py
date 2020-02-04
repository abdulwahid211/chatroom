from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__ , template_folder='../templates')
app.config['SECRET_KEY'] = 'vnkdjnfjwefdvsfvfdeknfl1232#'
socketio = SocketIO(app)

from chat_system import viewss