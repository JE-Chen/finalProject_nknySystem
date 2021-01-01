from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

Hash = RestfulAPIResource.Hash
ProfessorGrade = Blueprint('ProfessorGrade', __name__)


@ProfessorGrade.route(r'/GET/ProfessorGrade')
@cross_origin()
def professor_grade_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Professor'):
        return render_template('/Grade/ProfessorCheckGrade.html')
    else:
        return redirect(url_for('Login.login_page'))
