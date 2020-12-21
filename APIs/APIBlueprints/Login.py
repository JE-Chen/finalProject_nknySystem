from flask import Blueprint, redirect, render_template
from flask_cors import cross_origin

Login = Blueprint('Login', __name__)


@Login.route(r'/Login')
@cross_origin()
def login():
    return render_template('/LoginPage/Login.html')
