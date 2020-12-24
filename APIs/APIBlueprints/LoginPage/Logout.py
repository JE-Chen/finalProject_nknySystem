from flask import Blueprint, render_template
from flask_cors import cross_origin

Logout = Blueprint('Logout', __name__)


@Login.route(r'/Logout')
@cross_origin()
def login_page():
    return render_template('/LoginPage/Logout.html')
