import re
from flask import Flask, jsonify, render_template,request
import tensorflow as tf
import numpy as np
import datetime
from pandas.io.parsers import read_csv

class Cabbage:

    def __init__(self):
        pass

    @staticmethod
    def create():
        tf.global_variables_initializer()

        data = read_csv('./data/price data.csv', sep=',')

        xy = np.array(data, dtype=np.float32)

        x_data = xy[:, 1:-1]

        y_data = xy[:, [-1]]

        X = tf.placeholder(tf.float32, shape=[None, 4])
        Y = tf.placeholder(tf.float32, shape=[None, 1])

        W = tf.Variable(tf.random_normal([4, 1]), name="weight")
        b = tf.Variable(tf.random_normal([1]), name="bias")

        hypothesis = tf.matmul(X, W) + b

        cost = tf.reduce_mean(tf.square(hypothesis - Y))

        optomizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optomizer(cost)

        sess = tf.Session()

        sess.run(tf.global_variables_initializer())

        for step in range(100001):
            cost_, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
            if step % 500 == 0:
                print("#", step, " 손실비용:", cost)
                print("- 배추가격:", hypo_[0])

        saver = tf.train.Saver()
        saver.save(sess, "./data/saved.cpkt")
        print('학습된 모델을 저장했습니다.')

    @staticmethod
    def excute():
        X = tf.placeholder(tf.float32, shape=[None, 4])
        Y = tf.placeholder(tf.float32, shape=[None, 1])

        W = tf.Variable(tf.random_normal([4, 1]), name="weight")
        b = tf.Variable(tf.random_normal([1]), name="bias")

        hypothesis = tf.matmul(X, W) + b

        saver = tf.train.Saver()
        model = tf.global_variables_initializer()

        sess = tf.Session()
        sess.run(model)

        saver.restore(sess,save_path='./data/saved.cpkt')