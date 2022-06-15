let currentIndex = 0;
let nextIndex;

function slider(cIndex, nIndex){
    let firstSlide = document.getElementById("slide1");
    let secondSlide = document.getElementById("slide2");
    let thirdSlide = document.getElementById("slide3");
    let slideList = [firstSlide, secondSlide, thirdSlide];
    slideList[cIndex].style.display = "none";
    slideList[nIndex].style.display = "block";
}

function next() {
    if(currentIndex < 2) {
        nextIndex = currentIndex + 1;
    } else {
        nextIndex = 0;
    }
    slider(currentIndex, nextIndex);
    currentIndex = nextIndex;
}

function previous() {
    if(currentIndex > 0) {
        nextIndex = currentIndex - 1;
    } else {
        nextIndex = 2;
    }
    slider(currentIndex, nextIndex);
    currentIndex = nextIndex;
}

function autoSlider() {
    setInterval(next, 5000);
}