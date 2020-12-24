from flask import Blueprint, render_template
from flask_cors import cross_origin

ProfessorGrade = Blueprint('ProfessorGrade', __name__)


@ProfessorGrade.route(r'/ProfessorGrade')
@cross_origin()
def professor_grade_page():
    return render_template('/Grade/ProfessorCheckGrade.html')
