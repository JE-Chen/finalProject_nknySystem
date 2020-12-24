from flask import Blueprint, render_template
from flask_cors import cross_origin

StudentIndex = Blueprint('StudentIndex', __name__)


@StudentIndex.route(r'/StudentIndex')
@cross_origin()
def student_index_page():
    return render_template('/Index/StudentIndex.html')