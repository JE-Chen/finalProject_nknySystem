function Image_Base64(Component, Image_Base64) {
    $(Component).prop("src", Image_Base64);
    $(Component).show();
}


function Hide_Image(Component) {
    $(Component).hide();
}

function test() {
    $.ajax({
        url: 'http://127.0.0.1:5000/Test_Data',
        method: 'GET',
        error: function (err) {
            console.log(err.responseText)
        },
        success: function (res) {
            console.log(res);
            res = res.Data[0]
            console.log(res.test_data);
            console.log(res.test_name);
            console.log(res.test_key);

        }
    });
}


function Get_Code(Component) {
    const request = new XMLHttpRequest();
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            if (request.readyState === 4) {
                console.log(request.responseText);
                Image_Base64(Component, request.responseText)
            }
        } else {
            console.log('err');
        }
    }
    request.onerror = function () {
        console.log('error')
    }
    request.open('GET', '/LoginVerificationCode', true)
    request.send()
}
