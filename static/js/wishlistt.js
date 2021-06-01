$(function() {

    $(".backBtn").click(function() {

        $(".popup-emp").css({
            'visibility': 'hidden'
        })

    })

    $(".popup-emp").click(function() {

        $(".popup-emp").css({
            'visibility': 'hidden'
        })

    })
    $(".delete").click(function(e) {
        e.preventDefault()

        $(".popup-emp").css({
            'visibility': 'visible',
        })
        element = $(this).parent()

        $(".deleteBtn").click(function(e) {

            $(".popup-emp").css({
                'visibility': 'hidden'
            })


            element.remove()

            _productid = element.data("productid")

            $.ajax({
                url: "/deleteproduct/" + _productid,
                method: "GET",
                success: function(data) {

                    if (data.liked == 0) {
                        $(".heartProductNumber").html('<div class="notlikedEmp"><svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" class="pt-2"width="45" height="45"viewBox="0 0 172 172"style=" fill:#000000;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="none" stroke-linecap="none" stroke-linejoin="none" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter"></path><g stroke="#ffffff"><path d="M86.00344,141.04c-19.88664,-11.18516 -63.64344,-39.52732 -63.64344,-72.23484c0,-17.11572 8.42112,-30.82412 21.45872,-34.92976c2.55076,-0.80152 5.1514,-1.1954 7.7744,-1.1954c11.43456,0 23.2716,7.93092 32.8434,21.58256c0.71208,1.0234 2.42004,1.0234 3.12868,0c11.77168,-16.78376 26.93864,-24.68716 40.62124,-20.38716c13.03244,4.10564 21.45356,17.81404 21.45356,34.92976c0.00344,32.7144 -43.74992,61.04968 -63.63656,72.23484z" stroke-width="3.44" stroke-linecap="butt" stroke-linejoin="miter"></path><path d="M140.90584,59.34c-0.2752,-1.18852 -0.60544,-2.33576 -0.989,-3.44M141.87076,69.66c0.01892,-0.43516 0.02924,-0.87032 0.02924,-1.30548c0,-1.91952 -0.12556,-3.78228 -0.36636,-5.57452M138.4858,52.46c-2.7348,-5.54872 -6.98148,-9.56664 -12.26532,-11.22988c-9.89172,-3.10632 -21.65136,3.05644 -31.46912,17.0452c-1.92984,2.79156 -5.20472,4.49092 -8.72556,4.49436c-0.00344,0 -0.0086,0 -0.01204,0c-3.51912,0 -6.794,-1.69248 -8.76512,-4.53048c-8.08572,-11.52228 -17.64892,-17.8192 -26.19216,-17.8192c-1.78708,0 -3.56384,0.27348 -5.27868,0.81184c-9.52364,2.99452 -15.6778,13.64132 -15.6778,27.12096c0,27.04184 38.51252,52.92612 55.90344,63.2272c16.36752,-9.69564 51.4538,-33.196 55.51128,-58.48" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"></path></g></g></svg><span> Favori Ürününüz yok </span></div>')
                    } else {
                        $(".likeNumber").html(data.liked)

                    }


                }

            })

        })



    })




})