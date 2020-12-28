from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerStudentLessonList = Blueprint('ManagerStudentLessonList', __name__)


@ManagerStudentLessonList.route(r'/ManagerStudentLessonList')
@cross_origin()
def manager_student_lesson_list_page():
    if session.get('Login'):
        return render_template('/Manager/ManagerStudentLessonList.html')
    else:
        return redirect(url_for('Login.login_page'))
