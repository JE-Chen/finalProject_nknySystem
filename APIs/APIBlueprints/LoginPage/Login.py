from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_cors import cross_origin

from APIs.Resource import RestfulAPIResource

RestfulAPIResource = RestfulAPIResource

SQL = RestfulAPIResource.SQL
VerificationCode = RestfulAPIResource.VerificationCode
LogSystem = RestfulAPIResource.LogSystem

Login = Blueprint('Login', __name__)


@Login.route(r'/Login')
@cross_origin()
def login_page():
    return render_template('/LoginPage/Login.html')


@Login.route(r'/LoginVerificationCode')
@cross_origin()
def login_verification_code():
    if session.get('verification_code') is None:
        verification_code = VerificationCode.generate_base64_image(5, 40)
        session['verification_code'] = verification_code[0]
        session['verification_image'] = verification_code[1]
        LogSystem.debug(verification_code[0])
        LogSystem.debug(verification_code[1])
        return verification_code[1]
    else:
        return session.get('verification_image')


@Login.route(r'/LoginCheck', methods=['POST', ])
@cross_origin()
def login_check():
    if request.method == 'POST':
        SQL.table_name = 'Account'
        SQL.select_prefix = '*'
        PersonnelNumber = request.form.get('PersonnelNumber')
        Password = request.form.get('Password')
        verification_code = request.form.get('VerificationCode')
        print(verification_code)
        CheckAccount = SQL.select_account('PersonnelNumber', 'Password', PersonnelNumber, Password)
        LogSystem.warning(CheckAccount)
        if verification_code == session.get('verification_code'):
            session['verification_code'] = None
            session['verification_image'] = None
            if len(CheckAccount) == 1:
                SQL.select_prefix = 'PersonnelAccess.Access'
                Access = SQL.inner_join('PersonnelAccess', 'Account.PersonnelNumber', 'PersonnelAccess.PersonnelNumber')
                LogSystem.warning(Access)
                session['Login'] = True
                if Access[0] == 'Normal':
                    session['Access'] = 'Normal'
                    return redirect(url_for('StudentIndex.student_index_page'))
                elif Access[0] == 'Professor':
                    session['Access'] = 'Professor'
                    return redirect(url_for('ProfessorIndex.professor_index_page'))
                elif Access[0] == 'Super':
                    session['Access'] = 'Super'
                    return redirect(url_for('ManagerIndex.manager_index_page'))
    return redirect(url_for('Login.login_page'))
