from flask import Blueprint, render_template
from flask_cors import cross_origin

Verification = Blueprint('Verification', __name__)


@Verification.route(r'/Verification')
@cross_origin()
def verification_page():
    return render_template('/LoginPage/Verification.html')