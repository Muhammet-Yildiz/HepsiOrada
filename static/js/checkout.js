$(function() {


    $(window).scroll(function() {

        if ($(document).width() == 1519) {


            if ($(window).scrollTop() > 92) {

                $(".payed_prices_Emp").css({

                    'position': 'fixed',
                    'top': '55px ',
                    'right': '194px '
                })

            } else {

                $(".payed_prices_Emp").css({
                    'position': 'relative',
                    'top': '0 ',
                    'right': '0 '
                })
            }


        }



    })



    $(".addres").each(function(index, element) {
        if (index == 0) {

            $(element).addClass("checked")
            $(element).find("svg").css("display", "block")
        }
    })


    $(".addres").on("click", function() {

        var chooseAddress = $(this)[0]

        $(".addres").each(function(index, element) {


            $(element).removeClass("checked")
            $(element).find("svg").css("display", "none")

        })

        $(chooseAddress).addClass("checked")
        $(chooseAddress).find("svg").css("display", "block")


    })


    $('.contractCheck input').click(function() {
        if ($(this).is(':checked')) {

            $(".Payment_Area  ").css("z-index", "5")
            $(".Payment_Area  ").css("opacity", "1")
            $(".uyarı ").css("display", "none")


            $(".Payment_Area").each(function() {

                var number = $(this).children('.payment_received').length

                if (number == 1) {
                    $(".orderConfirmBtn").prop("disabled", false)
                    $(".orderConfirmBtn").css({
                        'background-color': '#FF6000',
                        'cursor': 'pointer'
                    })

                } else {
                    $(".orderConfirmBtn").prop("disabled", true)
                    $(".orderConfirmBtn").css({
                        'background-color': 'rgb(196, 196, 196)',
                        'cursor': 'not-allowed'
                    })

                }

            });


        } else {
            $(".Payment_Area  ").css("z-index", "-99")
            $(".Payment_Area  ").css("opacity", "0.2")
            $(".uyarı ").css("display", "inline-block")

            $(".orderConfirmBtn").prop("disabled", true)
            $(".orderConfirmBtn").css({
                'background-color': 'rgb(196, 196, 196)',
                'cursor': 'not-allowed'
            })
        }
    });



    $("#make-payment").click(function() {


        $(".Payment_Area").html($(".payment_received"))
        $(".payment_received").css({
            "display": "flex",
            'width': '860px '

        })

        $(".orderConfirmBtn").prop("disabled", false)
        $(".orderConfirmBtn").css({
            'background-color': '#FF6000',
            'cursor': 'pointer'
        })

    })






})