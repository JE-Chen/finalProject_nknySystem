from flask import Blueprint, render_template
from flask_cors import cross_origin

LessonList = Blueprint('LessonList', __name__)


@LessonList.route(r'/LessonList')
@cross_origin()
def lesson_list_page():
    return render_template('/Grade/LessonList.html')