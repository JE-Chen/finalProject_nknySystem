from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin

ManagerAccount = Blueprint('ManagerAccount', __name__)


@ManagerAccount.route(r'/GET/ManagerAccount')
@cross_origin()
def manager_account_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerAccount.html')
    else:
        return redirect(url_for('Login.login_page'))
