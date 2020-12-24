from flask import Blueprint, render_template
from flask_cors import cross_origin

ManagerStudentLessonList = Blueprint('ManagerStudentLessonList', __name__)


@ManagerStudentLessonList.route(r'/ManagerStudentLessonList')
@cross_origin()
def manager_student_lesson_list_page():
    return render_template('/Manager/ManagerStudentLessonList.html')