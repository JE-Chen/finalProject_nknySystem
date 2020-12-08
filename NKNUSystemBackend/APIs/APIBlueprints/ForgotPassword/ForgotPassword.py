from flask import request, redirect, Blueprint
from flask_cors import cross_origin

ForgotPassword = Blueprint('ForgotPassword', __name__)


@ForgotPassword.route(r'/ForgotPassword', methods=['GET', 'POST'])
@cross_origin()
def forgot_password_function():
    if request.method == "POST":
        print(request.form.get('Email'))
    return redirect('http://127.0.0.1:5000/Verification_Code', 302)

