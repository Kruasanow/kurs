from flask import Flask, request,jsonify
from random import choice
import sqlite3
from test import quotes, create, about_me, get_all_post, get_post_by_id, db_data_addiction, insert_data ,delete_data, update_data
from datetime import datetime

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

create()

@app.route("/quotes", methods=['POST'])
def get_all_quotes():
    res = get_all_post()
    return jsonify(res)

@app.route("/quotes/<int:quote_id>", methods=['GET'])
def get_one_quote(quote_id):
    res = get_post_by_id(quote_id)
    return jsonify(res)

@app.route("/quotes/<int:quote_id>", methods=["PUT"])
def edit_quote(quote_id):
    insert_data(quote_id,f'author+{datetime.now()}',f'text+{datetime.now()}')
    return f'id={quote_id}'

@app.route("/quotes/<int:quote_id>", methods=["POST"])
def update_quote(quote_id):
    update_data(quote_id,f'author+{datetime.now()}',f'text+{datetime.now()}')
    return f'id={quote_id}'

@app.route("/quotes/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
    delete_data(quote_id)
    return f'id={quote_id}'


if __name__ == "__main__":
   app.run(debug=True)