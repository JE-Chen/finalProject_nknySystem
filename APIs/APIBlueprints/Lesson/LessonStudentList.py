from flask import Blueprint, render_template
from flask_cors import cross_origin

LessonStudentList = Blueprint('LessonStudentList', __name__)


@LessonStudentList.route(r'/LessonStudentList')
@cross_origin()
def lesson_student_list_page():
    return render_template('/Lesson/LessonStudentList.html')