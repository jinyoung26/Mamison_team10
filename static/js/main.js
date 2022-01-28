function listing() {
    alert("message")
    $.ajax({
        type: 'GET',
        url: '/auto_recipe_write',
        data: {},
        success: function (response) {
            alert("message2")
            let rows = response['recipes']
            for (let i = 0; i < rows.length; i++) {
                let imgstyle = rows[i].select_one(' a > div')
                let imgsrl = imgstyle['style']
                list(imgsrl)
                let src = imgsrl.split(');')[0]
                src = src.split('url(')[1]
                src = src.split('`')[1]
                src = src.slice(0, -1);
                src = src.slice(1)
                let reple = rows[i].select_one('div.h_recipe_list_top > div.h_recipe_list_top_cont>p.h_recipe_list_top_cont_tit>a').text
                let name = rows[i].select_one('div.h_recipe_list_top > div.h_recipe_list_top_cont > p.h_recipe_list_top_cont_name>a').text
                let imga = rows[i].select_one('a>img')['src']
               alert(name)
                alert(imga)
                alert(reple)
                alert(src)

                let temp = `<li class ="rasipi_li_list">
                        <div class = "rasipi_img_box">
                            <a class ="rasipi_img">
                                  <img class ="rasipi-imgs" src = ../static/img/${src} >
                            </a>
                        </div>
                        <div class =rasipi_comant_box">
                            <div class="rasipi_commant">
                                      ${reple}
                           </div>
                           <div class = "name_box">
                                <img class ="name_img" src =../static/img/${imga}> "${name}"
                           </div>
                           <div class="rasipi_poot_box">
                                <span class ="heart_box" >
                                    <img  style="width: 14px; margin: 0; " src= ../static/img/like@4x.png>
                                    공감수
                                </span>
                                <span class ="heart_count">
                                        ${like}
                                </span>

                           </div>

                        </div>

                        </div>


                </li>`
                $('#rasipi_container').append(temp)

            }
        }
    })
}