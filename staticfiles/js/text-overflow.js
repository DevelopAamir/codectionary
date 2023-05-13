    //this for triming texts 
    var titles = document.getElementsByClassName('title-txt');
    for(var i = 0; i< titles.length; i++){
        if(titles[i].innerText.length > 50){
            titles[i].innerText = titles[i].innerText.substring(0, 50) + '  ....';
        }
        
    }