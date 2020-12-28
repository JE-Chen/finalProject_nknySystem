from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerStudentDetail = Blueprint('ManagerStudentDetail', __name__)


@ManagerStudentDetail.route(r'/ManagerStudentDetail')
@cross_origin()
def manager_student_detail_page():
    if session.get('Login'):
        return render_template('/Manager/ManagerStudentDetail.html')
    else:
        return redirect(url_for('Login.login_page'))