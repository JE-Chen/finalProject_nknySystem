from flask import Blueprint, render_template
from flask_cors import cross_origin

ManagerAccount = Blueprint('ManagerAccount', __name__)


@ManagerAccount.route(r'/ManagerAccount')
@cross_origin()
def manager_page():
    return render_template('/Manager/ManagerAccount.html')