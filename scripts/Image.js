function Image_Base64(Component, Image_Base64) {
    $(Component).attr("src", Image_Base64);
    $(Component).show();
}

function Change_Image(Component, Image_Path) {
    $(Component).show();
    $(Component).html('<img alt="Loading" src= ' + Image_Path + '>');
}

function Hide_Image(Component) {
    $(Component).hide();
}

function Get_Code(Component) {
    const request = new XMLHttpRequest();
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            if(request.readyState === 4)
            Image_Base64(Component, request.responseText)
        } else {
            console.log('err');
        }
    }
    request.onerror = function () {
        console.log('error')
    }
    request.open('GET', 'http://127.0.0.1:5000/Generate_CodeImage', true)
    request.send()
}