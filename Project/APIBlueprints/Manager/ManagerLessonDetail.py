import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

Hash = RestfulAPIResource.Hash
SQL = RestfulAPIResource.SQL
ManagerLessonDetail = Blueprint('ManagerLessonDetail', __name__)


@ManagerLessonDetail.route(r'/GET/ManagerLessonDetail')
@cross_origin()
def manager_lesson_detail_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerLessonDetail.html')
    else:
        return redirect(url_for('Login.login_page'))


@ManagerLessonDetail.route(r'/PUT/LessonDetail', methods=['POST', ])
@cross_origin()
def manager_edit_lesson_detail():
    if request.method == 'POST':
        if request.form.get('method') == 'PUT':
            SQL.table_name = 'LessonDetail'
            LessonCode = request.form.get('LessonCode')
            LessonName = request.form.get('LessonName')
            LessonCredit = request.form.get('LessonCredit')
            LessonProfessor = request.form.get('LessonProfessor')
            LessonType = request.form.get('LessonType')
            SQL.insert_into_replace(LessonCode, LessonName, LessonCredit, LessonProfessor, LessonType)
    return render_template('/Manager/ManagerLessonDetail.html')


@ManagerLessonDetail.route(r'/GET/LessonDetail', methods=['GET', ])
@cross_origin()
def manager_lesson_detail():
    SQL.table_name = 'LessonDetail'
    SQL.select_prefix = '*'
    Details = SQL.select_form()
    print(Details)
    return json.dumps(Details)


@ManagerLessonDetail.route(r'/DELETE/LessonDetail', methods=['POST', ])
@cross_origin()
def manager_remove_lesson_detail():
    if request.method == 'POST':
        if request.form.get('method') == 'DELETE':
            SQL.table_name = 'LessonDetail'
            for keys in request.values:
                if keys == 'method':
                    pass
                else:
                    SQL.delete('LessonCode', keys)
    return render_template('/Manager/ManagerLessonDetail.html')
