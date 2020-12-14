import os

from NKNUSystemBackend.APIs.APIBlueprints.ForgotPassword import ForgotPassword
from NKNUSystemBackend.APIs.APIBlueprints.Login import Login
from flask import Flask, session
from flask_cors import cross_origin

app = Flask(__name__)

app.register_blueprint(Login.Login)
app.register_blueprint(ForgotPassword.ForgotPassword)

app.secret_key = os.urandom(16)

'''
全部資料：GET + 名稱
特定資料：GET + 名稱 + id
新增一筆資料：POST + 名稱
修改特定資料：PUT + 名稱 + id
刪除特定資料：DELETE + 名稱 + id
'''


# 捕抓例外路徑
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return f'Path : {path} not exist'


@app.route(r'/', methods=['GET', 'POST'])
@cross_origin()
def main_page():
    if session.get("LoginState") is None:
        return "Not Login"
    return "Main"


if __name__ == "__main__":
    app.run(debug=True)
