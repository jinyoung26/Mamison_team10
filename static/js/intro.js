const body = document.querySelector("whole"); //call body tag

const photoNum = 3; //num of photo;

function callRan() {
    let ranNum = Math.floor((Math.random() * 6) + 1);//call number 1 to 6
    return ranNum
}

function callPho() {
    let ranNum = callRan();
    let url = `/static/img/logo${ranNum}.png`;
    body.style.backgroundImage = `url(${url})`;

}

function init() {
    callPho();
}
