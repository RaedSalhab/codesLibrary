let firstSlide = document.getElementById("slide1");
let secondSlide = document.getElementById("slide2");
let thirdSlide = document.getElementById("slide3");
let index = 0;
function sliding(){
    console.log("Done");
    if(index == 0) {
        document.getElementById("slide1").style.display = "none";
        document.getElementById("slide2").style.display = "block";
        index++
    } else if (index == 1) {
        document.getElementById("slide2").style.display = "none";
        document.getElementById("slide3").style.display = "block";
        index++
    } else if (index == 2) {
        document.getElementById("slide3").style.display = "none";
        document.getElementById("slide1").style.display = "block";
        index = 0
    }
}