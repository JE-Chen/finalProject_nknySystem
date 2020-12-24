from flask import Blueprint, render_template
from flask_cors import cross_origin

Verification = Blueprint('Verification', __name__)


@Login.route(r'/Verification')
@cross_origin()
def login_page():
    return render_template('/LoginPage/Verification.html')