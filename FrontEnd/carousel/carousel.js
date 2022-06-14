let next = 2;
function sliding(){
    let firstSlide = document.getElementById("slide1");
    let secondSlide = document.getElementById("slide2");
    let thirdSlide = document.getElementById("slide3");
    if(next == 2) {
        firstSlide.style.display = "none";
        secondSlide.style.display = "block";
        thirdSlide.style.display = "none";
        next = 3;
    } else if (next == 3) {
        firstSlide.style.display = "none";
        secondSlide.style.display = "none";
        thirdSlide.style.display = "block";
        next = 1;
    } else if (next == 1) {
        thirdSlide.style.display = "none";
        firstSlide.style.display = "block";
        secondSlide.style.display = "none";
        next = 2;
    }
}

function previous() {
    if(next == 1){
        next = 2;
    } else if(next == 2) {
        next = 3;
    } else if(next == 3){
        next = 1;
    }
    
    sliding();
}