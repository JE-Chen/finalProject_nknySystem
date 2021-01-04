import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

Hash = RestfulAPIResource.Hash
SQL = RestfulAPIResource.SQL
ProfessorGrade = Blueprint('ProfessorGrade', __name__)


@ProfessorGrade.route(r'/GET/ProfessorGrade')
@cross_origin()
def professor_grade_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Professor'):
        return render_template('/Grade/ProfessorGrade.html')
    else:
        return redirect(url_for('Login.login_page'))


@ProfessorGrade.route(r'/PUT/ProfessorStudentGrade', methods=['POST', ])
@cross_origin()
def professor_edit_student_grade():
    if request.method == 'POST':
        if request.form.get('method') == 'PUT':
            SQL.table_name = 'LessonGrade'
            LessonCode = request.form.get('LessonCode')
            PersonnelNumber = request.form.get('PersonnelNumber')
            Grade = request.form.get('Grade')
            Semester = request.form.get('Semester')
            LessonProfessor = request.form.get('LessonProfessor')
            SQL.insert_into_replace(PersonnelNumber, LessonCode, Grade, Semester, LessonProfessor)
    return render_template('/Grade/ProfessorGrade.html')


@ProfessorGrade.route(r'/GET/ProfessorStudentGrade', methods=['GET', ])
@cross_origin()
def professor_student_grade():
    SQL.table_name = 'PersonnelDetail'
    SQL.select_prefix = 'LessonGrade.LessonCode,LessonGrade.PersonnelNumber,LessonGrade.Grade,LessonGrade.Semester,LessonGrade.LessonProfessor'
    Lists = SQL.inner_join_where_and('LessonGrade',
                                     'PersonnelDetail.PersonnelName',
                                     'LessonGrade.LessonProfessor',
                                     'PersonnelDetail.PersonnelNumber',
                                     session.get('PersonnelNumber'),
                                     no_arg="no")
    print(Lists)
    return json.dumps(Lists)
