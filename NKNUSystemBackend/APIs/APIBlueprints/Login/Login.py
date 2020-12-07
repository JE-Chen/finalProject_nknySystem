from datetime import timedelta

from flask import request, redirect, session, Blueprint
from flask_cors import cross_origin

Login = Blueprint('Login', __name__)

@Login.route(r'/Login', methods=['GET', 'POST'])
@cross_origin()
def LoginFunction():
    session['LoginState'] = "Login"
    session.permanent = True
    Login.permanent_session_lifetime = timedelta(minutes=10)
    if request.method == "POST":
        print(request.form.get('Email'))
        print(request.form.get('Password'))
        print(request.form.get('Verification_Code'))
    return redirect('http://127.0.0.1:5000/', 302)


@Login.route(r'/Logout', methods=['GET'])
@cross_origin()
def LogoutFunction():
    if request.method == "POST":
        print(request.form.get('Email'))
        print(request.form.get('Password'))
        print(request.form.get('Verification_Code'))
    return redirect('http://127.0.0.1:5000/', 302)
