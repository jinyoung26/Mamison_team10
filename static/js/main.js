// let ras = [{
//     'img': 'back.gif',
//     'recipe_id': '마미',
//     'content': '오케이 계획대로 되고있어!',
//     'like_count': '1'
// }, {'img': 'gloves.PNG', 'recipe_id': '마미', 'content': '소년점프소년점프', 'like_count': '25'},
//     {'img': 'logo.PNG', 'recipe_id': '마미', 'content': '와다다다다다', 'like_count': '100'}, {
//         'img': 'mamiy_charic.png',
//         'recipe_id': '마미',
//         'content': '폭염에 복면쓰고 불구덩이에',
//         'like_count': '250'
//     }, {'img': 'logo.PNG', 'recipe_id': '마미', 'content': '박힌 내맘을 알아?', 'like_count': '300'}]
//
//
// rasipi(ras)
//
//
// function rasipi(data) {
//     let b = 1
//     for (a of data) {
//         let imgsrc = a['img']
//         let name = a['recipe_id']
//         let comment = a['content']
//         let like = a['like_count']
//         let temp = `<li class ="rasipi_li_list">
//                         <div class = "rasipi_img_box">
//                             <a class ="rasipi_img">
//                                   <img class ="rasipi-imgs" src = ../img/${imgsrc} >
//
//                             </a>
//                         </div>
//                         <div class =rasipi_comant_box">
//                             <div class="rasipi_commant">
//                                       ${comment}
//                            </div>
//                            <div class = "name_box">
//                                 <img class ="name_img" src =../img/${imgsrc}> "${name}"
//                            </div>
//                            <div class="rasipi_poot_box">
//                                 <span class ="heart_box" >
//                                     <img  style="width: 14px; margin: 0; " src= ../img/like@4x.png>
//                                     공감수
//                                 </span>
//                                 <span class ="heart_count">
//                                         ${like}
//                                 </span>
//
//                            </div>
//
//                         </div>
//
//                         </div>
//
//
//                 </li>`
//
//         console.log(temp)
//         console.log(document.getElementById('rasipi_container'))
//         $('#rasipi_container').append(temp)
//         b++
//     }
//
// }
//
// let dialog = document.getElementById('dialog');
//
let url ="https://www.10000recipe.com/recipe/list.html?cat1=&cat2=&cat3=&cat4=&order=reco&page=";
function goSearchRecipe(link,code){
    function get_url(link, code) {
        list(url)
        src = url.split(link)[0]
        src = src.concat(link).concat(code)
        src = src.concat(url.split(link)[1])
        url = src
        return src
    }

    switch (link){
        case "cat4":
            return get_url(link,code);
        case "cat3":
            return get_url(link,code)
        case "cat2":
            return get_url(link,code)
        case "cat1":
            return get_url(link,code)
        default:
            return "https://www.10000recipe.com/recipe/list.html?cat1=&cat2=&cat3=&cat4=&order=reco&page="
    }

}

