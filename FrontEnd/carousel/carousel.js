let firstSlide = document.getElementById("slide1");
let secondSlide = document.getElementById("slide2");
let thirdSlide = document.getElementById("slide3");
let index = 2;
function sliding(){
    if(index == 2) {
        document.getElementById("slide1").style.display = "none";
        document.getElementById("slide2").style.display = "block";
        document.getElementById("slide3").style.display = "none";
        index++
    } else if (index == 3) {
        document.getElementById("slide1").style.display = "none";
        document.getElementById("slide2").style.display = "none";
        document.getElementById("slide3").style.display = "block";
        index = 1;
    } else if (index == 1) {
        document.getElementById("slide3").style.display = "none";
        document.getElementById("slide1").style.display = "block";
        document.getElementById("slide2").style.display = "none";
        index = 2;
    }
}

function previous() {
    if(index == 1){
        index = 2;
    } else if(index == 2) {
        index = 3;
    } else if(index == 3){
        index = 1;
    }
    
    sliding();
}