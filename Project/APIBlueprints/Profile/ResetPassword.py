from flask import Blueprint, render_template, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

ResetPassword = Blueprint('ResetPassword', __name__)

SQL = RestfulAPIResource.SQL
Gmail = RestfulAPIResource.Gmail
VerificationCode = RestfulAPIResource.VerificationCode
Hash = RestfulAPIResource.Hash
LogSystem = RestfulAPIResource.LogSystem


@ResetPassword.route(r'/GET/ResetPassword')
@cross_origin()
def reset_password_page():
    return render_template('/Profile/ResetPassword.html')


@ResetPassword.route(r'/PUT/ResetPassword', methods=['POST', ])
@cross_origin()
def update_password():
    if request.method == 'POST':
        if request.form.get('method') == 'PUT':
            PersonnelNumber = request.form.get('PersonnelNumber')
            SQL.table_name = 'Account'
            SQL.select_prefix = '*'
            CheckAccount = SQL.select_where('PersonnelNumber', PersonnelNumber)
            LogSystem.debug(PersonnelNumber)
            if len(CheckAccount) > 0:
                Password = request.form.get('Password')
                PasswordAgain = request.form.get('PasswordAgain')
                LogSystem.debug(Password)
                LogSystem.debug(PasswordAgain)
                if Password == PasswordAgain:
                    SQL.update('Password', 'PersonnelNumber', Hash.hash_sha512(Password), PersonnelNumber)
        return render_template('/LoginPage/Login.html')
    else:
        return render_template('/LoginPage/Verification.html')
