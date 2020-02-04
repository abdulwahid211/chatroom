from chat_system import app
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'mysqld'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'chats'

mysql = MySQL(app)


