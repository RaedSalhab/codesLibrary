let view = false;
let state = false;
let droplist = false;

function navListFunc() {
    let navArea = document.getElementById("nav-area");
    if (view == false) {
        navArea.style.display = "block";
        view = true;
        state = true;
    }
    else {
        navArea.style.display = "none";
        view = false;
    }
}

function redisplay() {
    let navArea = document.getElementById("nav-area");
    let navBtn = document.getElementById("nav-btn");
    if (state == true) {
        navArea.style.display = "block";
    }
}

window.addEventListener("resize", redisplay);
