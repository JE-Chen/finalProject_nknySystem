from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerLessonDetail = Blueprint('ManagerLessonDetail', __name__)


@ManagerLessonDetail.route(r'/ManagerLessonDetail')
@cross_origin()
def manager_lesson_detail_page():
    if session.get('Login') == 'Login':
        return render_template('/Manager/ManagerLessonDetail.html')
    else:
        return redirect(url_for('Login.login_page'))
