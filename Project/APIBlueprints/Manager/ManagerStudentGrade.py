from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin
from Project.Resource import RestfulAPIResource

Hash = RestfulAPIResource.Hash
ManagerStudentGrade = Blueprint('ManagerStudentGrade', __name__)


@ManagerStudentGrade.route(r'/GET/ManagerStudentGrade')
@cross_origin()
def manager_student_grade_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerStudentGrade.html')
    else:
        return redirect(url_for('Login.login_page'))