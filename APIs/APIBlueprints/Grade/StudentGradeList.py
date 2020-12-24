from flask import Blueprint, render_template
from flask_cors import cross_origin

StudentGradeList = Blueprint('StudentGradeList', __name__)


@StudentGradeList.route(r'/StudentGradeList')
@cross_origin()
def student_grade_list_page():
    return render_template('/Grade/StudentGradeList.html')