import json

from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
StudentGradeList = Blueprint('StudentGradeList', __name__)


@StudentGradeList.route(r'/GET/StudentGradeList')
@cross_origin()
def student_grade_list_page():
    if session.get('Login') == 'Login':
        return render_template('/Grade/StudentGradeList.html')
    else:
        return redirect(url_for('Login.login_page'))


@StudentGradeList.route(r'/GET/StudentGradeList/PersonnelNumber', methods=['GET', ])
@cross_origin()
def manager_student_lesson_list():
    SQL.table_name = 'LessonGrade'
    SQL.select_prefix = '*'
    Lists = SQL.select_where('PersonnelNumber', session.get('PersonnelNumber'))
    print(Lists)
    return json.dumps(Lists)
