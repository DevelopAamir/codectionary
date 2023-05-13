//This is for all Videos
function showController(id){
    var ele = document.getElementById(id);
    ele.style.transition = ".5s";
    if(ele.hasAttribute('controls')){
        ele.removeAttribute('controls','');
    }else{
         ele.setAttribute('controls','');
    } 
}

function setRating(){
    var slide = document.getElementById('rate');
    var rate = document.getElementById('rated');
    rate.innerText = slide.value;
}

