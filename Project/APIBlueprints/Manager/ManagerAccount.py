import json

from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_cors import cross_origin

from Project.Resource import RestfulAPIResource

Hash = RestfulAPIResource.Hash
SQL = RestfulAPIResource.SQL
ManagerAccount = Blueprint('ManagerAccount', __name__)


@ManagerAccount.route(r'/GET/ManagerAccount')
@cross_origin()
def manager_account_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerAccount.html')
    else:
        return redirect(url_for('Login.login_page'))


@ManagerAccount.route(r'/GET/Account', methods=['GET', ])
@cross_origin()
def manager_account():
    SQL.table_name = 'Account'
    SQL.select_prefix = '*'
    Accounts = SQL.select_form()
    print(Accounts)
    return json.dumps(Accounts)


@ManagerAccount.route(r'/PUT/AddAccount', methods=['POST', ])
@cross_origin()
def manager_edit_account():
    if request.method == 'POST':
        if request.form.get('method') == 'PUT':
            SQL.table_name = 'Account'
            PersonnelNumber = request.form.get('PersonnelNumberAdd')
            if request.form.get('select_add_or_edit') == '新增':
                Password = request.form.get('PasswordAdd')
                if Password is None:
                    return render_template('/Manager/ManagerAccount.html')
                SQL.insert_into_replace(PersonnelNumber, Hash.hash_sha512(Password))
                SQL.table_name = 'PersonnelAccess'
                if request.form.get('select_access') == '學生帳號':
                    SQL.insert_into_replace(PersonnelNumber, Hash.hash_sha512('Normal'))
                elif request.form.get('select_access') == '教授帳號':
                    SQL.insert_into_replace(PersonnelNumber, Hash.hash_sha512('Professor'))
                return render_template('/Manager/ManagerAccount.html')
            elif request.form.get('select_add_or_edit') == '修改':
                PasswordEdit = request.form.get('PasswordEdit')
                if PasswordEdit is None:
                    return render_template('/Manager/ManagerAccount.html')
                SQL.table_name = 'Account'
                SQL.select_prefix = '*'
                Check = SQL.select_where('PersonnelNumber', PersonnelNumber)
                if len(Check) > 0:
                    SQL.update('Password', 'PersonnelNumber', Hash.hash_sha512(PasswordEdit), PersonnelNumber)
                return render_template('/Manager/ManagerAccount.html')
    return render_template('/Manager/ManagerAccount.html')


@ManagerAccount.route(r'/DELETE/Account', methods=['POST', ])
@cross_origin()
def manager_remove_account():
    if request.method == 'POST':
        if request.form.get('method') == 'DELETE':
            for keys in request.values:
                if keys == 'method':
                    pass
                else:
                    SQL.table_name = 'Account'
                    SQL.delete('PersonnelNumber', keys)
                    SQL.table_name = 'PersonnelAccess'
                    SQL.delete('PersonnelNumber', keys)
    return render_template('/Manager/ManagerAccount.html')
