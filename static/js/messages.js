async function showToast(msg){
    var widget = `<div class="toast-custom"><span></span>${msg}<img src="/static/img/close.svg" alt="" srcset=""></div>`;
    value = document.querySelectorAll('body')[0]
    value.innerHTML = value.innerHTML + widget;
    await new Promise(r => setTimeout(r, 2000));
    value.removeChild(value.lastChild);
}

