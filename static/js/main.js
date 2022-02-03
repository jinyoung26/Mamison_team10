let url ="http://127.0.0.1:8000/main?tag=cat1,cat2,cat3,cat4";
function goSearchRecipe(link,code){
    function get_url(link, code) {
        src = url.split(link)[0]
        src = src.concat(code)
        src = src.concat(url.split(link)[1])
        url = src
        return url
    }

    switch (link){
        case "cat4":
            location.href = get_url(link,code)
            break
        case "cat3":
            location.href = get_url(link,code)
            break
        case "cat2":
            location.href = get_url(link,code)
            break
        case "cat1":
            location.href = get_url(link,code)
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
