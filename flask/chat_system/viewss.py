from chat_system import app
from chat_system import socketio
from flask import jsonify, render_template
from data_config import mysql
import json

@app.route("/")
def sessions():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('user_connect')
def broadcast_to_all_new_users(response, methods=['GET','POST']):
    response = list()
    cur = mysql.connection.cursor()
    result = ''
    try:
        cur.execute("select * from messages;")
        result = cur.fetchall()  # fetches all the rows in a result set
    except:
        print('Error:Unable to fetch data.')
    cur.close()

    for x, y in result:
        print(str(x) +':'+ str(y))
        op = {"user_name":x,"message":y}
        response.append(op)
    response = json.dumps(response)
    print(response)
    socketio.emit('broadcast', response, callback=messageReceived)


@socketio.on('my event')
def handle_my_custom_event(response, methods=['GET', 'POST']):
    print('received my event: ' + str(response))
    print(response)

    try:
        _username = response["user_name"]
        _message = response["message"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO messages(name, message) VALUES (%s, %s)", (_username, _message))
        mysql.connection.commit()
    except KeyError:
        print("KeyError")

    socketio.emit('my response', response, callback=messageReceived)


