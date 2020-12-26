from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_cors import cross_origin

from APIs.Resource import RestfulAPIResource

RestfulAPIResource = RestfulAPIResource

SQL = RestfulAPIResource.SQL
VerificationCode = RestfulAPIResource.VerificationCode

Login = Blueprint('Login', __name__)


@Login.route(r'/Login')
@cross_origin()
def login_page():
    return render_template('/LoginPage/Login.html')


@Login.route(r'/LoginVerificationCode')
@cross_origin()
def login_verification_code():
    verification_code = VerificationCode.generate_base64_image(5, 40)
    session['verification_code'] = verification_code[0]
    print(verification_code)
    return verification_code[1]


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
        if verification_code == session.get('verification_code'):
            session['verification_code'] = False
            if len(CheckAccount) == 1:
                SQL.select_prefix = 'PersonnelAccess.Access'
                Access = SQL.inner_join('PersonnelAccess', 'Account.PersonnelNumber', 'PersonnelAccess.PersonnelNumber')
                if Access[0] == 'Normal':
                    return redirect(url_for('StudentIndex.student_index_page'))
                elif Access[0] == 'Professor':
                    return redirect(url_for('ProfessorIndex.professor_index_page'))
                elif Access[0] == 'Super':
                    return redirect(url_for('ManagerIndex.manager_index_page'))
    return redirect(url_for('Login.login_page'))
