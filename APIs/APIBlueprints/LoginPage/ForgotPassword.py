from flask import Blueprint, render_template
from flask_cors import cross_origin

ForgotPassword = Blueprint('ForgotPassword', __name__)


@Login.route(r'/ForgotPassword')
@cross_origin()
def login_page():
    return render_template('/LoginPage/ForgotPassword.html')