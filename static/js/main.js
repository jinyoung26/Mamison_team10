// $(function () {
//     let didScroll;
//     let lastScrollTop = 0;
//     const delta = 5; // 동작의 구현이 시작되는 위치
//     const navbarHeight = $(".main-header").outerHeight();
//
//     $(window).scroll(function (event) { // 스크롤시에 사용자가 스크롤했다는 것을 알림
//         didScroll = true;
//     });
//
//     setInterval(function () {  // hasScrolled()를 실행하고 didScroll 상태를 재설정
//         if (didScroll) {
//             hasScrolled();
//             didScroll = false;
//         }
//     }, 250);
//
//     function hasScrolled() {
//         const st = $(this).scrollTop(); // 접근하기 쉽게 현재 스크롤의 위치를 저장한다.
//
//         if (Math.abs(lastScrollTop - st) <= delta)
//             return; // 설정한 delta 값보다 더 스크롤되었는지를 확인한다.
//
// //헤더의 높이보다 더 스크롤되었는지 확인하고 스크롤의 방향이 위인지 아래인지를 확인한다.
// // If current position > last position AND scrolled past navbar...
//
//         if (st > lastScrollTop && st > navbarHeight) {
//             // Scroll Down
//             $(".main-header").f
//         } else {
//             // Scroll Up // If did not scroll past the document (possible on mac)...
//             if (st + $(window).height() < $(document).height()) {
//                 $(".main-header").slideUp("fast");
//             }
//         }
//
//         lastScrollTop = st;
//     }
// })

// 헤더 스크롤할 때 애니메이션 효과!
const headerContainer = document.querySelector('.main-header');
$(function () {
    window.addEventListener('scroll',
        function (e) {
            let scroll_position = window.scrollY;
            if (scroll_position!==0) {
                //console.log("wheel down");
                headerContainer.style.background = '#f5b335';
                headerContainer.style.transition = '0.5s';

            }
            else {
               headerContainer.style.background = 'linear-gradient(to bottom, rgba(0, 0, 0, 0.7) 10%, rgba(0, 0, 0, 0))';
               headerContainer.style.transition = '0.8s';
            }
        }
    );
})

let url = "http://127.0.0.1:8000/main?tag=cat1,cat2,cat3,cat4";

function goSearchRecipe(link, code) {
    function get_url(link, code) {
        src = url.split(link)[0]
        src = src.concat(code)
        src = src.concat(url.split(link)[1])
        url = src
        return url
    }

    switch (link) {
        case "cat4":
            location.href = get_url(link, code)
            break
        case "cat3":
            location.href = get_url(link, code)
            break
        case "cat2":
            location.href = get_url(link, code)
            break
        case "cat1":
            location.href = get_url(link, code)
            break
        default:
            return "http://127.0.0.1:8000/main?tag= 전체,전체,전체,전체"
    }

}


function eventHandler(e) {
    var $eTarget = $(e.currentTarget);
    // var $targetPanel = $('[aria-labelledby="' + $eTarget.attr('id') + '"]');
    $eTarget
        .attr('aria-selected', true)
        .addClass('active') // 구버전 IE
        .siblings('[role="tab"]')
        .attr('aria-selected', false)
        .removeClass('active'); // 구버전 IE

    // $targetPanel
    //     .attr('aria-hidden', false)
    //     .addClass('panel') // 구버전 IE
    //     .siblings('[role="tabpanel"]')
    //     .attr('aria-hidden', true)
    //     .removeClass('panel'); // 구버전 IE
}

// 이벤트 바인딩 - 이벤트와, 실행될 함수를 연결해줌
$('[role="tab"]').on('click', eventHandler);
//
