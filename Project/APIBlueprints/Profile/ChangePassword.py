from flask import Blueprint, render_template, redirect, session, url_for
from flask_cors import cross_origin

ChangePassword = Blueprint('ChangePassword', __name__)


@ChangePassword.route(r'/GET/ChangePassword')
@cross_origin()
def change_password_page():
    if session.get('Login') == 'Login':
        return render_template('/Profile/ChangePassword.html')
    else:
        return redirect(url_for('Login.login_page'))