import re
from flask import Flask, jsonify, render_template,request
import tensorflow as tf
import numpy as np
import datetime
from pandas.io.parsers import read_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():

    return jsonify()

if __name__ == '__main__':
    app.run()


