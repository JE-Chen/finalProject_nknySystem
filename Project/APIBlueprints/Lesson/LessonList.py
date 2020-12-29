from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

LessonList = Blueprint('LessonList', __name__)


@LessonList.route(r'/LessonList')
@cross_origin()
def lesson_list_page():
    if session.get('Login') == 'Login':
        return render_template('/Lesson/LessonList.html')
    else:
        return redirect(url_for('Login.login_page'))
