from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerSpawnStudentGrade = Blueprint('ManagerSpawnStudentGrade', __name__)


@ManagerSpawnStudentGrade.route(r'/ManagerSpawnStudentGrade')
@cross_origin()
def manager_spawn_student_grade_page():
    if session.get('Login'):
        return render_template('/Manager/ManagerSpawnStudentGrade.html')
    else:
        return redirect(url_for('Login.login_page'))
