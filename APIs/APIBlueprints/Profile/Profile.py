from flask import Blueprint, render_template
from flask_cors import cross_origin

Profile = Blueprint('Profile', __name__)


@Profile.route(r'/Profile')
@cross_origin()
def profile_page():
    return render_template('/Profile/Profile.html')