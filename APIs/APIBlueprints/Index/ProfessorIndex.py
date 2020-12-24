from flask import Blueprint, render_template
from flask_cors import cross_origin

ProfessorIndex = Blueprint('ProfessorIndex', __name__)


@ProfessorIndex.route(r'/ProfessorIndex')
@cross_origin()
def professor_index_page():
    return render_template('/Grade/ProfessorIndex.html')