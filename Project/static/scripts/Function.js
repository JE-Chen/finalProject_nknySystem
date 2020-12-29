function Image_Base64(Component, Image_Base64) {
    $(Component).prop("src", Image_Base64);
    $(Component).show();
}

function table_reset(method, url, component) {
    $.ajax({
        url: url,
        method: method,
        error: function (err) {
            console.log(err.responseText)
        },
        success: function (res) {
            let count = Object.keys(res).length
            res = res.Data[0]
            for (let i = 0; i < count; i++) {
                $(component).append(
                    '<tbody>' +
                    '<tr>' +
                    '<th scope="row">' +
                    '<input name= ' + res.test_name + ' type="checkbox">' +
                    '</th>' +
                    '<td>' + res.test_data + '</td>' +
                    '<td>' + res.test_name + '</td>' +
                    '<td>' + res.test_key + '</td>' +
                    '</tr>' +
                    '</tbody>'
                )
            }
        }
    });
}


function Ajax(method, url, eventCode, event, component) {
    const request = new XMLHttpRequest();
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            if (request.readyState === 4) {
                switch (eventCode) {
                    case 'AjaxCode':
                        event(component, request.responseText);
                        break;
                    case 'AjaxTable':
                        break
                    case 'AjaxTest':
                        let test = request.responseText
                        console.log(test)
                        console.log(typeof (test))
                        let JsonTest = JSON.parse(test)
                        console.log(JsonTest)
                        console.log(typeof (JsonTest))
                        for(let i=0;i<JsonTest.length;i++) {
                            let a = JsonTest[i]
                            console.log(JsonTest[i])
                            for(let j=0;j<a.length;j++)
                                console.log(a[j])
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