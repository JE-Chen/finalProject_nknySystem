from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

Logout = Blueprint('Logout', __name__)


@Logout.route(r'/GET/Logout')
@cross_origin()
def logout_page():
    session['Login'] = None
    return render_template('/LoginPage/Logout.html')
