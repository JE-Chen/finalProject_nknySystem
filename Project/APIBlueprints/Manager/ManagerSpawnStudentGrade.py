import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
Hash = RestfulAPIResource.Hash
ManagerSpawnStudentGrade = Blueprint('ManagerSpawnStudentGrade', __name__)


@ManagerSpawnStudentGrade.route(r'/GET/ManagerSpawnStudentGrade')
@cross_origin()
def manager_spawn_student_grade_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerSpawnStudentGrade.html')
    else:
        return redirect(url_for('Login.login_page'))


@ManagerSpawnStudentGrade.route(r'/GET/ManagerSpawnStudentGradeContent', methods=['GET', ])
@cross_origin()
def student_list():
    SQL.table_name = 'LessonGrade'
    SQL.select_prefix = '*'
    PersonnelNumber = request.args.get('PersonnelNumber')
    if PersonnelNumber is None:
        PersonnelNumber = '410877027'
    GradeContents = SQL.select_where('PersonnelNumber', PersonnelNumber)
    print(GradeContents)
    session['GradeContents'] = GradeContents
    return render_template('/Manager/ManagerSpawnStudentGrade.html')


@ManagerSpawnStudentGrade.route(r'/GET/ManagerSpawnStudentGrade/AJAX', methods=['GET', ])
@cross_origin()
def spawn_student_list():
    data = session.get('GradeContents')
    if data is None:
        return redirect(url_for('ManagerSpawnStudentGrade.manager_spawn_student_grade_page'))
    else:
        return json.dumps(data)
