from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ProfessorIndex = Blueprint('ProfessorIndex', __name__)


@ProfessorIndex.route(r'/GET/ProfessorIndex')
@cross_origin()
def professor_index_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Professor'):
        return render_template('/Index/ProfessorIndex.html')
    else:
        return redirect(url_for('Login.login_page'))
