from flask import Blueprint, render_template
from flask_cors import cross_origin

ProfessorCheckGrade = Blueprint('ProfessorCheckGrade', __name__)


@ProfessorCheckGrade.route(r'/ProfessorCheckGrade')
@cross_origin()
def professor_check_grade_page():
    return render_template('/Grade/ProfessorCheckGrade.html')