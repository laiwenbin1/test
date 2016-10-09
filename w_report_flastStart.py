# coding=utf-8
from flask import Flask, render_template, request, jsonify , session
#from crypt_module import NJ_encryptor
# from pyelasticsearch import ElasticSearch
import json, math
from pymongo import MongoClient
from bson.objectid import ObjectId
#from mock_create import MockCreate
from w_report_1 import *
from sign import *
import os


app = Flask(__name__)
app.secret_key =  os.urandom(24)

@app.route('/pie')
def pie_index():
    return render_template("report.html" , data_pie = getMedicalData() )


@app.route('/column')
def index():
    return render_template("column.html" , data_column = get_occurrence() )

##dneglu
@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/accounts/login',methods=['GET', 'POST'])
def accountsLogin():
    print "post"
    dict = {"username": "username","password1": "password1"}
    if request.method == 'POST':
        dict["username"]  = request.form['login']
        dict["password1"] = request.form['password']
    else:
        dict["username"] = request.args.get('login')
        dict["password1"] = request.args.get('password')
    result =  UserSingnIn(dict);
    if (result != -1 and result != -2):
        session["username"] = dict.get("username")
        session["password"] = dict["password1"]
        session["allMassage"] = dict
    return render_template('signin-test.html')


# 注册页面 Return 注册页面
@app.route('/signup')
def signup():
    return render_template('signup.html')

#csrfmiddlewaretoken=vflE1EZFFdpF4vyD2Y4HrLVHYegBa2YT&username=&email=&password1=
@app.route('/form-signin',methods=['GET', 'POST'])
def signup_user():
    dict = {"username": "apple", "email": "banana", "password1": "grape"}
    if request.method == 'POST':
        dict["username"] = request.form['username']
        dict["email"] = request.form['email']
        dict["password1"] = request.form['password1']
    else:
        dict["username"] = request.args.get('username')
        dict["email"] = request.args.get('email')
        dict["password1"] = request.args.get('password1')

    result = UserSingnUp(dict);
    if(result != -1 and result != -2):
        session["username"] = dict.get("username")
        session["password"] = dict["password1"]
        session["allMassage"] = dict

    return render_template("signin-test.html" ,succeedSigniUp = dict )

@app.route('/outer-page')
def test():
    return render_template("page-test.html")


if __name__ == "__main__":
    app.run()