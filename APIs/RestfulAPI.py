import os
from datetime import timedelta

from flask import Flask, session, url_for, redirect
from flask_cors import cross_origin

# Grade
from APIs.APIBlueprints.Grade import ProfessorCheckGrade
from APIs.APIBlueprints.Grade import ProfessorGrade
from APIs.APIBlueprints.Grade import StudentGrade
from APIs.APIBlueprints.Grade import StudentGradeList
# Index
from APIs.APIBlueprints.Index import ManagerIndex
from APIs.APIBlueprints.Index import ProfessorIndex
from APIs.APIBlueprints.Index import StudentIndex
# Lesson
from APIs.APIBlueprints.Lesson import LessonList
from APIs.APIBlueprints.Lesson import LessonStudentList
# LoginPage
from APIs.APIBlueprints.LoginPage import ForgotPassword
from APIs.APIBlueprints.LoginPage import Login
from APIs.APIBlueprints.LoginPage import Logout
from APIs.APIBlueprints.LoginPage import Verification
# Manager
from APIs.APIBlueprints.Manager import ManagerAccount
from APIs.APIBlueprints.Manager import ManagerLessonDetail
from APIs.APIBlueprints.Manager import ManagerSpawnStudentGrade
from APIs.APIBlueprints.Manager import ManagerStudentDetail
from APIs.APIBlueprints.Manager import ManagerStudentGrade
from APIs.APIBlueprints.Manager import ManagerStudentLessonList
# Profile
from APIs.APIBlueprints.Profile import ChangePassword
from APIs.APIBlueprints.Profile import Profile

app = Flask(__name__)

app.secret_key = os.urandom(16)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=3)
app.config["SESSION_PERMANENT"] = False

app.register_blueprint(ForgotPassword.ForgotPassword)
app.register_blueprint(Login.Login)
app.register_blueprint(Logout.Logout)
app.register_blueprint(Verification.Verification)

app.register_blueprint(ProfessorCheckGrade.ProfessorCheckGrade)
app.register_blueprint(ProfessorGrade.ProfessorGrade)
app.register_blueprint(StudentGrade.StudentGrade)
app.register_blueprint(StudentGradeList.StudentGradeList)

app.register_blueprint(ManagerIndex.ManagerIndex)
app.register_blueprint(ProfessorIndex.ProfessorIndex)
app.register_blueprint(StudentIndex.StudentIndex)

app.register_blueprint(LessonList.LessonList)
app.register_blueprint(LessonStudentList.LessonStudentList)

app.register_blueprint(ManagerAccount.ManagerAccount)
app.register_blueprint(ManagerLessonDetail.ManagerLessonDetail)
app.register_blueprint(ManagerStudentGrade.ManagerStudentGrade)
app.register_blueprint(ManagerStudentDetail.ManagerStudentDetail)
app.register_blueprint(ManagerSpawnStudentGrade.ManagerSpawnStudentGrade)
app.register_blueprint(ManagerStudentLessonList.ManagerStudentLessonList)

app.register_blueprint(ChangePassword.ChangePassword)
app.register_blueprint(Profile.Profile)

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


@app.route(r'/GET/MainPageHTML')
@cross_origin()
def main_page_html():
    Access = session.get('Access')
    if Access == 'Normal':
        session['Access'] = 'Normal'
        return redirect(url_for('StudentIndex.student_index_page'))
    elif Access == 'Professor':
        session['Access'] = 'Professor'
        return redirect(url_for('ProfessorIndex.professor_index_page'))
    elif Access == 'Super':
        session['Access'] = 'Super'
        return redirect(url_for('ManagerIndex.manager_index_page'))
    return redirect(url_for('Login.login_page'))


if __name__ == "__main__":
    app.debug = True
    # app.run(host='0.0.0.0', port=80)
    app.run()
