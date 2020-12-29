import json

from flask import Blueprint, render_template
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

ForgotPassword = Blueprint('ForgotPassword', __name__)

SQL = RestfulAPIResource.SQL
Gmail = RestfulAPIResource.Gmail
verification_code = RestfulAPIResource.VerificationCode
Hash = RestfulAPIResource.Hash


@ForgotPassword.route(r'/ForgotPassword')
@cross_origin()
def forgot_password_page():
    return render_template('/LoginPage/ForgotPassword.html')


@ForgotPassword.route(r'/ForgotPassword/GET/Gmail', methods=['POST', ])
@cross_origin()
def forgot_password_gmail():
    '''
    if request.method == 'POST':
        verification_code.generate_base64_image(5, 40, True)
        PersonnelNumber = request.form.get('PersonnelNumber')
        Email = request.form.get('Email')
    else:
    '''
    SQL.table_name = 'Account'
    SQL.select_prefix = '*'
    CheckAccount = SQL.select_account('PersonnelNumber', 'Password', '410877027', Hash.hash_sha512('test'))
    print(CheckAccount)
    return json.dumps([('410877001', 'Professor'), ('410877014', 'Normal'), ('410877027', 'Super')])
