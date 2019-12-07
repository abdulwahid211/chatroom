from app import app
from flask import jsonify 

@app.route("/apple")
def apple():
    return jsonify(username="Abzy211")


    