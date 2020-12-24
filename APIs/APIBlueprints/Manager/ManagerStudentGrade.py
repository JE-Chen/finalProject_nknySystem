from flask import Blueprint, render_template
from flask_cors import cross_origin

ManagerStudentGrade = Blueprint('ManagerStudentGrade', __name__)


@ManagerStudentGrade.route(r'/ManagerStudentGrade')
@cross_origin()
def manager_student_grade_page():
    return render_template('/Manager/ManagerStudentGrade.html')