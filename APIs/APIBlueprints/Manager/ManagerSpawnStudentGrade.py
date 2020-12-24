from flask import Blueprint, render_template
from flask_cors import cross_origin

ManagerSpawnStudentGrade = Blueprint('ManagerSpawnStudentGrade', __name__)


@ManagerSpawnStudentGrade.route(r'/ManagerSpawnStudentGrade')
@cross_origin()
def manager_spawn_student_grade_page():
    return render_template('/Manager/ManagerSpawnStudentGrade.html')
