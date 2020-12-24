from flask import Blueprint, render_template
from flask_cors import cross_origin

ManagerStudentDetail = Blueprint('ManagerStudentDetail', __name__)


@ManagerStudentDetail.route(r'/ManagerStudentDetail')
@cross_origin()
def manager_student_detail_page():
    return render_template('/Manager/ManagerStudentDetail.html')