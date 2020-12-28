from flask import Blueprint, render_template, redirect, session, url_for
from flask_cors import cross_origin

ChangePassword = Blueprint('ChangePassword', __name__)


@ChangePassword.route(r'/ChangePassword')
@cross_origin()
def change_password_page():
    return render_template('/Profile/ChangePassword.html')