from flask import Blueprint, render_template
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

ResetPassword = Blueprint('ResetPassword', __name__)

SQL = RestfulAPIResource.SQL
Gmail = RestfulAPIResource.Gmail
VerificationCode = RestfulAPIResource.VerificationCode
Hash = RestfulAPIResource.Hash


@ResetPassword.route(r'/GET/ResetPassword')
@cross_origin()
def reset_password_page():
    return render_template('/LoginPage/ResetPassword.html')


@ResetPassword.route(r'/PUT/ResetPassword')
@cross_origin()
def update_password():
    return render_template('/LoginPage/ResetPassword.html')
