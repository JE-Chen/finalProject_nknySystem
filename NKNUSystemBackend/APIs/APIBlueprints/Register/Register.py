from flask import request, redirect, Blueprint
from flask_cors import cross_origin
Register = Blueprint('Register', __name__)

@Register.route(r'/Register', methods=['GET', 'POST'])
@cross_origin()
def RegisterFunction():
    if request.method == "POST":
        print(request.form.get('Email'))
        print(request.form.get('Password'))
        print(request.form.get('ConfirmPassword'))
    return redirect('http://127.0.0.1:5000/Login', 302)


@Register.route(r'/ForgotPassword', methods=['GET', 'POST'])
@cross_origin()
def ForgotPasswordFunction():
    if request.method == "POST":
        print(request.form.get('Email'))
    return redirect('http://127.0.0.1:5000/Verification_Code', 302)


@Register.route(r'/VerificationCode', methods=['GET', 'POST'])
@cross_origin()
def VerificationCodeFunction():
    if request.method == "POST":
        print(request.form.get('Verification_Code'))
    return redirect('http://127.0.0.1:5000/Login', 302)


@Register.route(r'/GenerateCodeImage', methods=['GET', 'POST'])
@cross_origin()
def CodeImageFunction():
    pass
