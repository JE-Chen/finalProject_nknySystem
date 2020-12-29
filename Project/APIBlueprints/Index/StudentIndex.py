from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

StudentIndex = Blueprint('StudentIndex', __name__)


@StudentIndex.route(r'/StudentIndex')
@cross_origin()
def student_index_page():
    if session.get('Login') == 'Login':
        return render_template('/Index/StudentIndex.html')
    else:
        return redirect(url_for('Login.login_page'))
