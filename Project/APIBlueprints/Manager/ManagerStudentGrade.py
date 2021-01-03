import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
Hash = RestfulAPIResource.Hash
ManagerStudentGrade = Blueprint('ManagerStudentGrade', __name__)


@ManagerStudentGrade.route(r'/GET/ManagerStudentGrade/Page')
@cross_origin()
def manager_student_grade_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerStudentGrade.html')
    else:
        return redirect(url_for('Login.login_page'))


@ManagerStudentGrade.route(r'/PUT/ManagerStudentGrade', methods=['POST', ])
@cross_origin()
def manager_edit_student_lesson_list():
    if request.method == 'POST':
        if request.form.get('method') == 'PUT':
            SQL.table_name = 'LessonGrade'
            LessonCode = request.form.get('LessonCode')
            PersonnelNumber = request.form.get('PersonnelNumber')
            Grade = request.form.get('Grade')
            Semester = request.form.get('Semester')
            LessonProfessor = request.form.get('LessonProfessor')
            SQL.insert_into_replace(LessonCode, PersonnelNumber, Grade, Semester, LessonProfessor)
    return render_template('/Manager/ManagerStudentGrade.html')


@ManagerStudentGrade.route(r'/GET/ManagerStudentGrade', methods=['GET', ])
@cross_origin()
def manager_student_lesson_list():
    SQL.table_name = 'LessonGrade'
    SQL.select_prefix = '*'
    Lists = SQL.select_form()
    print(Lists)
    return json.dumps(Lists)
