function onBannerSelected(value){
    var banner = document.getElementById('banner');
    const reader = new FileReader();
    reader.addEventListener('load',()=>
    {
        document.getElementById('img-space').style.backgroundImage = `url(${reader.result})`;
    })
    reader.readAsDataURL(banner.files[0]);
   
}
 function onprofileSelected(value){
    var profile = document.getElementById('profile');
    
    const reader = new FileReader();
    reader.addEventListener('load',()=>
    {
        document.getElementById('select-profile').style.backgroundImage = `url(${reader.result})`;
    });
    reader.readAsDataURL(profile.files[0]);
   
}

function onNameChanged(value){
   
    var name = document.getElementById('setted-name');
    name.innerHTML = value;
    if(value == ''){
        name.innerHTML = 'Channel Name';
    }
}

function closemessage(id) {
    var doc = document.getElementById(id);
    doc.style.display= 'none';
}