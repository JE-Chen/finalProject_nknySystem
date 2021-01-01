from flask import Blueprint, render_template, redirect, session, request, url_for
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

Verification = Blueprint('Verification', __name__)

LogSystem = RestfulAPIResource.LogSystem


@Verification.route(r'/Verification')
@cross_origin()
def verification_page():
    return render_template('/LoginPage/Verification.html')


@Verification.route(r'/GET/Verification/Reset')
@cross_origin()
def verification_redirect_page():
    if request.method == 'GET':
        code = session.get('ForgotPasswordVerificationCode')
        if code is not None:
            print(request.args.get('Verification_Code'))
            if request.args.get('Verification_Code') == code:
                return redirect(url_for('ResetPassword.reset_password_page'))
        return render_template('/LoginPage/Verification.html')
    else:
        return render_template('/LoginPage/Verification.html')
