from flask import Blueprint, render_template
from flask_cors import cross_origin

Login = Blueprint('Login', __name__)


@Login.route(r'/Login')
@cross_origin()
def login_page():
    return render_template('/LoginPage/Login.html')


@Login.route(r'/LoginCheck')
@cross_origin()
def login_check():
    pass
