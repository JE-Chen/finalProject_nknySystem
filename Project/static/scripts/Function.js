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
                        let tableText = request.responseText
                        let jsonText = JSON.parse(tableText)
                        for (let i = 0; i < jsonText.length; i++) {
                            let a = jsonText[i]
                            $(component).append(
                                '<tbody>' +
                                '<tr>' +
                                '<th scope="row">' +
                                '<input name= ' + a[0] + ' type="checkbox">' +
                                '</th>' +
                                '<td>' + a[0] + '</td>' +
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