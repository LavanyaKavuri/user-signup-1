from flask import Flask, request, redirect, render_template
import os
import re,random


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('login_form.html')

def is_empty(str):
    if len(str) == 0:
        return 0
    else:
        return 1

def is_alphabet(str):
    if re.match(r'^\w+$',str):
        return 0
    else:
        return 1

def checkemail(str):
    if str == '@' or str == '.' or str == '':
        return 0
    else:
        return 1    

 
    
@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    #print (username)
    userpass = request.form['userpass']
    passverify = request.form['passverify']
    useremail = request.form['useremail']
    user_name_error = ''
    user_password_error = ''
    password_verify_error = ''
    user_email_error = ''

    if not is_empty(username):
        user_name_error = "Username not entered"
    else:
        if len(username) > 20 or len(username) < 3 or is_alphabet(username):
            user_name_error = " The range for username is 3 - 20 characters"
    
    if not is_empty(userpass):
        user_password_error = "Password not entered"
    else:
        if len(userpass) > 20 or len(userpass) < 3 or is_alphabet(userpass):
            user_password_error = " Invalid password "

    if passverify != userpass or not is_empty(passverify):
        password_verify_error = " Password and confirm password do not match"

    #if checkemail(username) or len(useremail) > 20 or len(useremail) < 3 :
    if checkemail(useremail) or len(useremail) > 20 or len(useremail) < 3 :
        user_email_error = "Please enter a valid email address"

    if not  user_name_error and not user_password_error and not password_verify_error and not user_email_error:
        return render_template('base.html',username=username)
    else:
        return render_template('login_form.html', username=username, 
            user_name_error=user_name_error, userpass=userpass,user_password_error=user_password_error,
            passverify=passverify,password_verify_error=password_verify_error,useremail=useremail,
            user_email_error=user_email_error)

app.run()
