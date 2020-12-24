from flask import Blueprint, render_template
from flask_cors import cross_origin

ManagerIndex = Blueprint('ManagerIndex', __name__)


@StudentGradeList.route(r'/ManagerIndex')
@cross_origin()
def manager_index_page():
    return render_template('/Grade/ManagerIndex.html')