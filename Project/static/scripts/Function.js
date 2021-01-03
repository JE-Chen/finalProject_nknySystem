function Image_Base64(Component, Image_Base64) {
    $(Component).prop("src", Image_Base64);
    $(Component).show();
}

function Ajax(method, url, eventCode, component, event) {
    const request = new XMLHttpRequest();
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            if (request.readyState === 4) {
                switch (eventCode) {

                    case 'AjaxCode':
                        event(component, request.responseText);
                        break;

                    case 'AjaxTable_ManagerAccount':
                        let ManagerAccountTableText = request.responseText
                        let ManagerAccountJsonText = JSON.parse(ManagerAccountTableText)
                        for (let i = 0; i < ManagerAccountJsonText.length; i++) {
                            let ManagerAccount = ManagerAccountJsonText[i]
                            $(component).append(
                                '<tbody>' +
                                '<tr>' +
                                '<th scope="row">' +
                                '<input name= ' + ManagerAccount[0] + ' type="checkbox">' +
                                '</th>' +
                                '<td>' + ManagerAccount[0] + '</td>' +
                                '</tr>' +
                                '</tbody>'
                            )
                        }
                        break

                    case 'AjaxTable_ManagerStudentDetail':
                        let ManagerStudentDetailTableText = request.responseText
                        let ManagerStudentDetailJsonText = JSON.parse(ManagerStudentDetailTableText)
                        for (let i = 0; i < ManagerStudentDetailJsonText.length; i++) {
                            let ManagerStudentDetail = ManagerStudentDetailJsonText[i]
                            $(component).append(
                                '<tbody>' +
                                '<tr>' +
                                '<th scope="row">' +
                                '<input name= ' + ManagerStudentDetail[0] + ' type="checkbox">' +
                                '</th>' +
                                '<td>' + ManagerStudentDetail[0] + '</td>' +
                                '<td>' + ManagerStudentDetail[1] + '</td>' +
                                '<td>' + ManagerStudentDetail[2] + '</td>' +
                                '</tr>' +
                                '</tbody>'
                            )
                        }
                        break

                    case 'AjaxTable_ManagerLessonDetail':
                        let ManagerLessonDetailTableText = request.responseText
                        let ManagerLessonDetailJsonText = JSON.parse(ManagerLessonDetailTableText)
                        for (let i = 0; i < ManagerLessonDetailJsonText.length; i++) {
                            let ManagerLessonDetail = ManagerLessonDetailJsonText[i]
                            $(component).append(
                                '<tbody>' +
                                '<tr>' +
                                '<th scope="row">' +
                                '<input name= ' + ManagerLessonDetail[0] + ' type="checkbox">' +
                                '</th>' +
                                '<td>' + ManagerLessonDetail[0] + '</td>' +
                                '<td>' + ManagerLessonDetail[1] + '</td>' +
                                '<td>' + ManagerLessonDetail[2] + '</td>' +
                                '<td>' + ManagerLessonDetail[3] + '</td>' +
                                '<td>' + ManagerLessonDetail[4] + '</td>' +
                                '</tr>' +
                                '</tbody>'
                            )
                        }
                        break

                    case 'AjaxTable_LessonList':
                        console.log(request.responseText);
                        let LessonListTableText = request.responseText
                        let LessonListJsonText = JSON.parse(LessonListTableText)
                        for (let i = 0; i < LessonListJsonText.length; i++) {
                            let ManagerLessonDetail = LessonListJsonText[i]
                            $(component).append(
                                '<tbody>' +
                                '<tr>' +
                                '<th>' + ManagerLessonDetail[0] + '</th>' +
                                '<td>' + ManagerLessonDetail[1] + '</td>' +
                                '<td>' + ManagerLessonDetail[2] + '</td>' +
                                '<td>' + ManagerLessonDetail[3] + '</td>' +
                                '</tr>' +
                                '</tbody>'
                            )
                        }
                        break

                    case 'AjaxTable_StudentLessonList':
                        console.log(request.responseText);
                        let StudentLessonListTableText = request.responseText
                        let StudentLessonListJsonText = JSON.parse(StudentLessonListTableText)
                        for (let i = 0; i < StudentLessonListJsonText.length; i++) {
                            let StudentLessonList = StudentLessonListJsonText[i]
                            $(component).append(
                                '<tbody>' +
                                '<tr>' +
                                '<th scope="row">' +
                                '<input name= ' + StudentLessonList[0] + ' type="checkbox">' +
                                '</th>' +
                                '<td>' + StudentLessonList[0] + '</td>' +
                                '<td>' + StudentLessonList[1] + '</td>' +
                                '<td>' + StudentLessonList[2] + '</td>' +
                                '</tr>' +
                                '</tbody>'
                            )
                        }
                        break

                    case 'AjaxTable_StudentGrade':
                        console.log(request.responseText);
                        let StudentGradeTableText = request.responseText
                        let StudentGradeJsonText = JSON.parse(StudentGradeTableText)
                        for (let i = 0; i < StudentGradeJsonText.length; i++) {
                            let StudentLessonList = StudentGradeJsonText[i]
                            $(component).append(
                                '<tbody>' +
                                '<tr>' +
                                '<td>' + StudentLessonList[0] + '</td>' +
                                '<td>' + StudentLessonList[1] + '</td>' +
                                '<td>' + StudentLessonList[2] + '</td>' +
                                '<td>' + StudentLessonList[3] + '</td>' +
                                '<td>' + StudentLessonList[4] + '</td>' +
                                '</tr>' +
                                '</tbody>'
                            )
                        }
                        break
                }
            }
        }
    }
    request.onerror = function () {
        console.log('error')
    }
    request.open(method, url, true)
    request.send()

}