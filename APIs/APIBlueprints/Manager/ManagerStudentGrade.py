from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerStudentGrade = Blueprint('ManagerStudentGrade', __name__)


@ManagerStudentGrade.route(r'/ManagerStudentGrade')
@cross_origin()
def manager_student_grade_page():
    if session.get('Login'):
        return render_template('/Manager/ManagerStudentGrade.html')
    else:
        return redirect(url_for('Login.login_page'))