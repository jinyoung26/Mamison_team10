// $(document).ready(function () {
//     $(".idol").click(function () {
//         $("#whole").css('background-image', 'linear-gradient( rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3) ), url("/static/img/egg.gif")');
//         $("#whole").css('background-size', 'contain');
//         $("#whole").css('background-position', 'center');
//     })
// });

// $(document).ready(function () {
//     let randomNumber = Math.floor(Math.random() * 3);
//     let imgName = '/static/img/' + ['korean-food2.jpg', 'egg.gif', 'kimbap.jpg'];
//     $("#whole").backgroundImage.css(imgName(randomNumber))
// });

$(document).ready(function () {
    $(".idol").click(function () {
        let randomNumber = Math.floor(Math.random() * 5);
        let imgName = ['takoyaki.jpg','teokboki.jpg','teokguk.jpg','waffle.jpg', 'egg.gif'];
        let imgPath = ('/static/img/' + imgName[randomNumber]);
        $("#whole").css('background-image', 'linear-gradient( rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3) ), url("' + imgPath + '")');
        $("#whole").css('background-size', 'cover');
        $("#whole").css('background-position', 'center');
    })
});
