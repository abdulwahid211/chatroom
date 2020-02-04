
from chat_system import app
from chat_system import socketio

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=False)

