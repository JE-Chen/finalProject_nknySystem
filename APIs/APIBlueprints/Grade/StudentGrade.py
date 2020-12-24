from flask import Blueprint, render_template
from flask_cors import cross_origin

StudentGrade = Blueprint('StudentGrade', __name__)


@StudentGrade.route(r'/StudentGrade')
@cross_origin()
def student_grade_page():
    return render_template('/Grade/StudentGrade.html')