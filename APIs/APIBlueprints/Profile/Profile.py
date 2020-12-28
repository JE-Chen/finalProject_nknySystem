from flask import Blueprint, render_template, redirect, session, url_for
from flask_cors import cross_origin

Profile = Blueprint('Profile', __name__)


@Profile.route(r'/Profile')
@cross_origin()
def profile_page():
    if session.get('Login'):
        return render_template('/Profile/Profile.html')
    else:
        return redirect(url_for('Login.login_page'))


