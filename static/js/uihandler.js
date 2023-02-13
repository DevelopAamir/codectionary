// This is to remove the unnessecery subbscription logo from the landing page

var subs = document.getElementsByClassName('mbl-subs');
for(var i = 0; i < subs.length; i++){
    if(i >= 5){
        subs[i].style.display  = 'none';
    }
}

//This is to remove search icon from input fields
var inputField = document.getElementById('search');
var icon = document.getElementById('searchIcon');
inputField.addEventListener('input', updateValue);
function updateValue(e) {
    if(inputField.value != ''){
        icon.style.visibility = 'hidden';

    }
    if(inputField.value == ''){
        icon.style.visibility = 'visible';
    }
}

//this is to arrange last video
var w = window.innerWidth;
if(w >= 1400){
    var videoos = document.getElementsByClassName('videoCard');
    videoos[videoos.length - 1].setAttribute('style', 'margin-left: 10px')
}

