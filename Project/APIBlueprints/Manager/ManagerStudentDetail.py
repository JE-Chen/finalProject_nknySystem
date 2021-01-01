from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin
from Project.Resource import RestfulAPIResource

Hash = RestfulAPIResource.Hash
ManagerStudentDetail = Blueprint('ManagerStudentDetail', __name__)


@ManagerStudentDetail.route(r'/GET/ManagerStudentDetail')
@cross_origin()
def manager_student_detail_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerStudentDetail.html')
    else:
        return redirect(url_for('Login.login_page'))