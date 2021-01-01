from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerSpawnStudentGrade = Blueprint('ManagerSpawnStudentGrade', __name__)


@ManagerSpawnStudentGrade.route(r'/GET/ManagerSpawnStudentGrade')
@cross_origin()
def manager_spawn_student_grade_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerSpawnStudentGrade.html')
    else:
        return redirect(url_for('Login.login_page'))
