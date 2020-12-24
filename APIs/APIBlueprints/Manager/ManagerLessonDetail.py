from flask import Blueprint, render_template
from flask_cors import cross_origin

ManagerLessonDetail = Blueprint('ManagerLessonDetail', __name__)


@ManagerLessonDetail.route(r'/ManagerLessonDetail')
@cross_origin()
def manager_lesson_detail_page():
    return render_template('/Manager/ManagerLessonDetail.html')
