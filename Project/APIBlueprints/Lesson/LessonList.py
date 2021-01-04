import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
LessonList = Blueprint('LessonList', __name__)


@LessonList.route(r'/GET/LessonList')
@cross_origin()
def lesson_list_page():
    if session.get('Login') == 'Login':
        return render_template('/Lesson/LessonList.html')
    else:
        return redirect(url_for('Login.login_page'))


@LessonList.route(r'/GET/LessonListContent', methods=['GET', ])
@cross_origin()
def lesson_list():
    SQL.table_name = 'LessonContent'
    SQL.select_prefix = '*'
    Semester = request.args.get('Semester')
    if Semester is None:
        Semester = '109'
    LessonContents = SQL.select_where('Semester', Semester)
    print(LessonContents)
    session['LessonContents'] = LessonContents
    return render_template('/Lesson/LessonList.html')


@LessonList.route(r'/GET/LessonListContent/AJAX', methods=['GET', ])
@cross_origin()
def get_lesson_list():
    data = session.get('LessonContents')
    if data is None:
        return redirect(url_for('LessonList.lesson_list_page'))
    else:
        return json.dumps(data)
