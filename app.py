import re
from flask import Flask, jsonify, render_template,request
import tensorflow as tf
import numpy as np
import datetime
from pandas.io.parsers import read_csv
from db import Database
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return jsonify()

@app.route('/login',methods=['POST'])
def login():
    print('---------------로그인 들어옴----------------')
    db = Database()
    #db.drop_table()
    #db.create()
    #db.insert_many()

    userid = request.form['userid']
    password = request.form['password']

    print('아이디는 {}, 비번 {}'.format(userid,password))


    row = db.login(userid,password)
    print('회원정보{}'.format(row))
    return render_template("main.html")

if __name__ == '__main__':
    app.run()


