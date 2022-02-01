# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import sqlite3
import json
from urllib import response
import numpy as np 
import flask
import h5py
from flask import request, redirect, url_for,flash, jsonify, render_template
from flask_wtf import Form
import pandas as pd
from pandas import ExcelFile
from sqlalchemy import VARCHAR
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model, model_from_json
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from sklearn.preprocessing import MinMaxScaler


app = flask.Flask(__name__,template_folder='templates')
app.secret_key = "super secret key"
model = None
# con = sqlite3.connect('model/creditscore.db')
# con.row_factory = sqlite3.Row








@app.route('/')
def indexpage():
    return flask.render_template("index.html")


@app.route('/dashboard')
def dashboard():
    con = sqlite3.connect('model/creditscore.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    

    cur.execute("select count(*) from customer")

    rows = cur.fetchall();
    print(rows)

    return flask.render_template("index.html", rows=rows)


@app.route('/tables')
def table():
    
    con = sqlite3.connect('model/creditscore.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
   
    cur.execute("SELECT * FROM customer")

    rows = cur.fetchall();
        
        
    return flask.render_template('tables.html', rows=rows)
    

# @app.route('/tables')
# def table(phoneNumber):
    # if request.method =='POST':

        
    #         pn=request.form['phoneNumber']
            
    #         con = sqlite3.connect('model/creditscore.db')
    #         con.row_factory = sqlite3.Row

    #         cur = con.cursor()
    #         cur.execute("SELECT * FROM customer WHERE phoneNumber=?", (pn,))         
    #         rows = cur.fetchall();

    #         return flask.render_template('tables.html',  rows=rows)
        
        
    
    # else:
    # con = sqlite3.connect('model/creditscore.db')
    # con.row_factory = sqlite3.Row

    # cur = con.cursor()
   
    # cur.execute("SELECT * FROM customer")

    # rows = cur.fetchall();
    # return flask.render_template('tables.html', rows=rows)
            

# @app.route('/api/data')
# def data():
#     return {'data': [user.to_dict() for user in User.query]}


@app.route('/predict', methods=['GET', 'POST'])
def predict():  
    global model
    
    if request.method ==  'POST':
       
        phoneNumber = request.form['phoneNumber']
        age = request.form['age']
        gender = request.form['gender']
        planType = request.form['planType']
        tenure = request.form['tenure']
        deviceOwned = request.form['deviceOwned']
        numCalls = request.form['numCalls']
        numSMS = request.form['numSMS']
        dataUsage = float(request.form['dataUsage'])
        monthlyFee = float(request.form['monthlyFee'])
        totalFee = float(request.form['totalFee'])
        overduePay = request.form['overduePay']
        barSuspend = request.form['barSuspend']
        creditScore = request.form['creditScore']


        #  display data
        display = [age, planType,tenure,deviceOwned, numCalls, numSMS, dataUsage,monthlyFee,totalFee,overduePay, 
                  barSuspend, creditScore]
        
        # df = pd.DataFrame(data)
        
        if (planType == "Postpaid"):
            planType=1
        else:
            planType=0

        # planType=int(planType)
        data = [age, planType,tenure,deviceOwned, numCalls, numSMS, dataUsage,monthlyFee,totalFee,overduePay, 
                barSuspend, creditScore]        
        cols_to_scale = [[age,tenure,deviceOwned, numCalls, numSMS, dataUsage,monthlyFee,totalFee,overduePay, 
                        barSuspend, creditScore]]
        scaler = MinMaxScaler()
        cols=scaler.fit_transform(cols_to_scale)
        json_file = open('model/creditscore_model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        if model == None :
            model = loaded_model.load_weights("model/creditscore_weights.h5")
            print("Loaded model from disk")

            p = model.predict(cols)
        #prediction = model.predict([[age, planType, tenure, deviceOwned, numCalls, numSMS, dataUsage, monthlyFee, totalFee, overduePay, barSuspend,creditScore]])
            global y_pred
            y_pred=[]
            for element in p:
                if element > 0.5:
                    y_pred.append('Approved')
                else:
                    y_pred.append('Rejected')

            print(y_pred)
        pred = pd.DataFrame(y_pred)

        # # print(prediction)
        # result = pd.concat([display, pred], axis=1)

        # print(result)


        #cols = scaler.fit_transform(data[cols_to_scale])
        
        return render_template('predict.html')
        # if(prediction=="N"):
        #     prediction="No"
        # else:
        #     prediction="Yes"


    #     return render_template("prediction.html", prediction_text="loan status is {}".format(prediction))
    # else:
    #     return render_template("prediction.html")

    return flask.render_template("predict.html")

# @app.route("/pred",y_pred=y_pred)
# def resPred():
#   return Response(predict()) 

if __name__ == "_main_":
    app.debug = True
    app.run()



