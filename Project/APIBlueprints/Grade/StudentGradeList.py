from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

StudentGradeList = Blueprint('StudentGradeList', __name__)


@StudentGradeList.route(r'/GET/StudentGradeList')
@cross_origin()
def student_grade_list_page():
    if session.get('Login') == 'Login':
        return render_template('/Grade/StudentGradeList.html')
    else:
        return redirect(url_for('Login.login_page'))
