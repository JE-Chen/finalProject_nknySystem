from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

LessonStudentList = Blueprint('LessonStudentList', __name__)


@LessonStudentList.route(r'/GET/LessonStudentList')
@cross_origin()
def lesson_student_list_page():
    if session.get('Login') == 'Login':
        return render_template('/Lesson/LessonStudentList.html')
    else:
        return redirect(url_for('Login.login_page'))

