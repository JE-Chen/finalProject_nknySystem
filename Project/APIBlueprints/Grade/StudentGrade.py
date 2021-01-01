from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

StudentGrade = Blueprint('StudentGrade', __name__)


@StudentGrade.route(r'/GET/StudentGrade')
@cross_origin()
def student_grade_page():
    if session.get('Login') == 'Login':
        return render_template('/Grade/StudentGrade.html')
    else:
        return redirect(url_for('Login.login_page'))
