import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
Hash = RestfulAPIResource.Hash
ManagerStudentLessonList = Blueprint('ManagerStudentLessonList', __name__)


@ManagerStudentLessonList.route(r'/GET/ManagerStudentLessonList')
@cross_origin()
def manager_student_lesson_list_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerStudentLessonList.html')
    else:
        return redirect(url_for('Login.login_page'))


@ManagerStudentLessonList.route(r'/PUT/StudentLessonList', methods=['POST', ])
@cross_origin()
def manager_edit_student_lesson_list():
    if request.method == 'POST':
        if request.form.get('method') == 'PUT':
            SQL.table_name = 'SemesterLesson'
            LessonCode = request.form.get('LessonCode')
            PersonnelNumber = request.form.get('PersonnelNumber')
            Semester = request.form.get('Semester')
            SQL.insert_into_replace(LessonCode, PersonnelNumber, Semester)
    return render_template('/Manager/ManagerStudentLessonList.html')


@ManagerStudentLessonList.route(r'/GET/StudentLessonList', methods=['GET', ])
@cross_origin()
def manager_student_lesson_list():
    SQL.table_name = 'SemesterLesson'
    SQL.select_prefix = '*'
    Lists = SQL.select_form()
    print(Lists)
    return json.dumps(Lists)


@ManagerStudentLessonList.route(r'/DELETE/StudentLessonList', methods=['POST', ])
@cross_origin()
def manager_remove_student_lesson_list():
    if request.method == 'POST':
        if request.form.get('method') == 'DELETE':
            SQL.table_name = 'SemesterLesson'
            for keys in request.values:
                if keys == 'method':
                    pass
                else:
                    SQL.delete('LessonCode', keys)
    return render_template('/Manager/ManagerStudentLessonList.html')
