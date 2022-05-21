
function progressFunc(){
    console.log("work1");
    const progressBar = document.getElementById("progress");
    let interval = null;
    let widthValue = 0;
    let viewValue;
    clearInterval(interval);
    interval = setInterval(bar, 100);
    function bar() {
        if (widthValue >= 300) {
            clearInterval(interval);
        }
        else {
            widthValue++;
            progressBar.style.width = widthValue + "px";
            viewValue = Math.round((widthValue / 300) * 100);
            progressBar.innerHTML = viewValue + "%";
        }
    }
}
