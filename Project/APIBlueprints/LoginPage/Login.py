from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

SQL = RestfulAPIResource.SQL
VerificationCode = RestfulAPIResource.VerificationCode
LogSystem = RestfulAPIResource.LogSystem
Hash = RestfulAPIResource.Hash

Login = Blueprint('Login', __name__)


@Login.route(r'/Login')
@cross_origin()
def login_page():
    return render_template('/LoginPage/Login.html')


@Login.route(r'/GET/LoginVerificationCode')
@cross_origin()
def login_verification_code():
    if request.method == 'GET':
        if session.get('verification_code') is None:
            verification_code = VerificationCode.generate_base64_image(5, 40)
            session['verification_code'] = verification_code[0]
            session['verification_image'] = verification_code[1]
            LogSystem.debug(verification_code[0])
            LogSystem.debug(verification_code[1])
            return verification_code[1]
        else:
            return session.get('verification_image')
    return redirect(url_for('Login.login_page'))


@Login.route(r'/GET/LoginCheck')
@cross_origin()
def login_check():
    if request.method == 'GET':
        SQL.table_name = 'Account'
        SQL.select_prefix = '*'
        PersonnelNumber = request.args.get('PersonnelNumber')
        Password = request.args.get('Password')
        verification_code = request.args.get('VerificationCode')
        Password = Hash.hash_sha512(Password)
        CheckAccount = SQL.select_account('PersonnelNumber', 'Password', PersonnelNumber, Password)
        LogSystem.debug(Password)
        LogSystem.debug(CheckAccount)
        if verification_code == session.get('verification_code'):
            session['verification_code'] = None
            session['verification_image'] = None
            if len(CheckAccount) == 1:
                SQL.select_prefix = 'PersonnelAccess.Access'
                Access = SQL.inner_join_where_distinct('PersonnelAccess',
                                                       request.args.get('PersonnelNumber'),
                                                       'PersonnelAccess.PersonnelNumber',
                                                       'Account.PersonnelNumber',
                                                       request.args.get('PersonnelNumber'))
                LogSystem.warning(Access)
                session['Login'] = 'Login'
                session['PersonnelNumber'] = PersonnelNumber
                if Access[0] == Hash.hash_sha512('Normal'):
                    session['Access'] = Hash.hash_sha512('Normal')
                    LogSystem.warning('Login Normal')
                    return redirect(url_for('StudentIndex.student_index_page'))
                elif Access[0] == Hash.hash_sha512('Professor'):
                    session['Access'] = Hash.hash_sha512('Professor')
                    LogSystem.warning('Login Professor')
                    return redirect(url_for('ProfessorIndex.professor_index_page'))
                elif Access[0] == Hash.hash_sha512('Super'):
                    session['Access'] = Hash.hash_sha512('Super')
                    LogSystem.warning('Login Super')
                    return redirect(url_for('ManagerIndex.manager_index_page'))
    return redirect(url_for('Login.login_page'))
