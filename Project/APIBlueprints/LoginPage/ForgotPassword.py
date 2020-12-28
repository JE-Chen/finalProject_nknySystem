from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ForgotPassword = Blueprint('ForgotPassword', __name__)


@ForgotPassword.route(r'/ForgotPassword')
@cross_origin()
def forgot_password_page():
    return render_template('/LoginPage/ForgotPassword.html')
