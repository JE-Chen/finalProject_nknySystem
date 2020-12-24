from flask import Blueprint, render_template
from flask_cors import cross_origin

Logout = Blueprint('Logout', __name__)


@Logout.route(r'/Logout')
@cross_origin()
def logout_page():
    return render_template('/LoginPage/Logout.html')
