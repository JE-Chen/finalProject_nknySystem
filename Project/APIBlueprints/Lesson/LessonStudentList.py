import json

from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
LessonStudentList = Blueprint('LessonStudentList', __name__)


@LessonStudentList.route(r'/GET/LessonStudentList')
@cross_origin()
def lesson_student_list_page():
    if session.get('Login') == 'Login':
        return render_template('/Lesson/LessonStudentList.html')
    else:
        return redirect(url_for('Login.login_page'))


@LessonStudentList.route(r'/GET/LessonStudentListContent', methods=['GET', ])
@cross_origin()
def student_list():
    SQL.table_name = 'SemesterLesson'
    SQL.select_prefix = '*'
    Semester = request.args.get('Semester')
    if Semester is None:
        Semester = '109'
    LessonContents = SQL.select_where('Semester', Semester)
    print(LessonContents)
    session['LessonContents'] = LessonContents
    return render_template('/Lesson/LessonStudentList.html')


@LessonStudentList.route(r'/GET/LessonStudentList/AJAX', methods=['GET', ])
@cross_origin()
def get_student_list():
    data = session.get('LessonContents')
    if data is None:
        return redirect(url_for('LessonStudentList.lesson_student_list_page'))
    else:
        return json.dumps(data)
