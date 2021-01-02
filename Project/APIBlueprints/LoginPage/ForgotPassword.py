import os

from flask import Blueprint, render_template, redirect, session, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

ForgotPassword = Blueprint('ForgotPassword', __name__)

SQL = RestfulAPIResource.SQL
Gmail = RestfulAPIResource.Gmail
VerificationCode = RestfulAPIResource.VerificationCode
Hash = RestfulAPIResource.Hash


@ForgotPassword.route(r'/GET/ForgotPassword')
@cross_origin()
def forgot_password_page():
    return render_template('/LoginPage/ForgotPassword.html')


@ForgotPassword.route(r'/GET/ForgotPassword/GET/Gmail')
@cross_origin()
def forgot_password_gmail():
    if request.method == 'GET':
        verification_code = VerificationCode.generate_base64_image(5, 40, True)
        PersonnelNumber = request.args.get('PersonnelNumber')
        Email = request.args.get('Email')
        SQL.select_prefix = '*'
        SQL.table_name = 'Account'
        CheckAccount = SQL.select_where('PersonnelNumber', PersonnelNumber)
        if len(CheckAccount) > 0:
            with open(os.getcwd() + '/NKNUSystemBackend/Tests/GmailTest/Templates/Email_Template1_Picture.html',
                      'r+') as File:
                content = (File.read())
            Gmail.Gmail_API.send_mail_attach("410877027@mail.nknu.edu.tw", Email, "忘記密碼驗證信",
                                             content,
                                             attach_file=os.getcwd() + '/code_image.jpeg',
                                             use_html=True)
            File.close()
            session['ForgotPasswordVerificationCode'] = verification_code[0]
            print(verification_code[0])
            return redirect(url_for('Verification.verification_page'))
    else:
        return redirect(url_for('ForgotPassword.forgot_password_page'))
