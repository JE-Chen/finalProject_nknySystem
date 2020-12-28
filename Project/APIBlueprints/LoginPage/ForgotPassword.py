from flask import Blueprint, render_template, redirect
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

ForgotPassword = Blueprint('ForgotPassword', __name__)

Gmail = RestfulAPIResource.Gmail
verification_code = RestfulAPIResource.VerificationCode


@ForgotPassword.route(r'/ForgotPassword')
@cross_origin()
def forgot_password_page():
    return render_template('/LoginPage/ForgotPassword.html')


@ForgotPassword.route(r'/ForgotPassword/GET/Gmail', methods=['POST', ])
@cross_origin()
def forgot_password_gmail():
    if request.method == 'POST':
        verification_code.generate_base64_image(5, 40, True)
    return redirect(url_for('ForgotPassword.forgot_password_page'))
