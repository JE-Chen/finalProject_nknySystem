import os

from flask import Flask
from flask_cors import cross_origin

# LoginPage
from APIs.APIBlueprints.LoginPage import ForgotPassword
from APIs.APIBlueprints.LoginPage import Login
from APIs.APIBlueprints.LoginPage import Logout
from APIs.APIBlueprints.LoginPage import Verification

# Grade
from APIs.APIBlueprints.Grade import ProfessorCheckGrade
from APIs.APIBlueprints.Grade import ProfessorGrade
from APIs.APIBlueprints.Grade import StudentGrade
from APIs.APIBlueprints.Grade import StudentGradeList

# Index
from APIs.APIBlueprints.Index import ManagerIndex
from APIs.APIBlueprints.Index import ProfessorIndex
from APIs.APIBlueprints.Index import StudentIndex

# Manager
from APIs.APIBlueprints.Manager import ManagerAccount
from APIs.APIBlueprints.Manager import ManagerLessonDetail
from APIs.APIBlueprints.Manager import ManagerStudentGrade
from APIs.APIBlueprints.Manager import ManagerStudentDetail
from APIs.APIBlueprints.Manager import ManagerSpawnStudentGrade
from APIs.APIBlueprints.Manager import ManagerStudentLessonList

# Profile
from APIs.APIBlueprints.Profile import ChangePassword
from APIs.APIBlueprints.Profile import Profile

app = Flask(__name__)

app.secret_key = os.urandom(16)
app.register_blueprint(Login.Login)
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


@app.route(r'/')
@cross_origin()
def main_page():
    return 'Success'


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
    # app.run()
