import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
Hash = RestfulAPIResource.Hash
ProfessorCheckGrade = Blueprint('ProfessorCheckGrade', __name__)


@ProfessorCheckGrade.route(r'/GET/ProfessorCheckGrade')
@cross_origin()
def professor_check_grade_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Professor'):
        return render_template('/Grade/ProfessorCheckGrade.html')
    else:
        return redirect(url_for('Login.login_page'))


@ProfessorCheckGrade.route(r'/GET/ProfessorCheckStudentGrade', methods=['GET', ])
@cross_origin()
def professor_check_grade():
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
