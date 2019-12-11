from app import app
from flask import jsonify, request
from flask_mysqldb import MySQL


app.config['MYSQL_HOST'] = 'docker-local-mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'gymbuddy'

mysql = MySQL(app)

@app.route("/apple", methods=['POST'])
def apple():
    if request.method == "POST":
        firstName = request.form['fname']
        lastName = request.form['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return jsonify(fname=firstName,lastName=lastName)
    
    
    return jsonify(username="Abzy211")


    