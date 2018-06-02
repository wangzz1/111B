from flask import Flask,url_for,request,redirect,render_template
from manage import User,Blog,app

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        pass#show_the_loginform()

