from chat_system import app
from chat_system import socketio
from flask import render_template
from data_config import mysql
import json

@app.route("/")
def sessions():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(response, methods=['GET', 'POST']):
    print('received my event: ' + str(response))
    print(response)

    format = json.dumps(response)
    data = json.loads(format)
    try:
        _username = data["user_name"]
        _message = data["message"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO messages(name, message) VALUES (%s, %s)", (_username, _message))
        mysql.connection.commit()
    except KeyError:
        print("KeyError")

    socketio.emit('my response', response, callback=messageReceived)
