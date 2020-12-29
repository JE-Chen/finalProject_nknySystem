from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ProfessorIndex = Blueprint('ProfessorIndex', __name__)


@ProfessorIndex.route(r'/ProfessorIndex')
@cross_origin()
def professor_index_page():
    if session.get('Login') == 'Login':
        return render_template('/Index/ProfessorIndex.html')
    else:
        return redirect(url_for('Login.login_page'))
