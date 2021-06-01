$(function() {
    $(".lineIcon").on("click", function() {

        console.log("naber ")

        $(".min_fixed-p").toggleClass("visibility")

    })
    $(".closeIcon").on("click", function() {
        console.log("naber22 ")

        $(".min_fixed-p").addClass("visibility")

    })



    $(".update-cart").click(function() {
        var value = $(".itemsayısı").html()
        if (parseInt(value) == 0) {
            $(".itemsayısı").html("1")
            console.log(typeof value);
            console.log("girdi ")

        } else {

            newvalue = parseInt(value) + 1

            $(".itemsayısı").html(newvalue)
        }
    })



    $("#hesabım").on("mouseover", function() {


        $("#account_options").css("display", "inline-block")

    })
    $("#hesabım").mouseout(function() {

        $("#account_options").css("display", "none")

    })


    $("#login-register").on("mouseover", function() {


        $("#log_regis_options").css("display", "inline-block")

    })
    $("#login-register").mouseout(function() {

        $("#log_regis_options").css("display", "none")

    })




    $("#tagss").click(function() {

        $(this).css({

            'border': '2px solid #FF6000',
            'background-color': 'white'
        })

    })
    $("#tagss").blur(function() {

        $(this).css({
            'background-color': ' #F3F3F3',
            'border': 'none'

        })

    })


    $(".closeIcon").click(function() {

        $(".min_fixed-p").css("display", "none")

    })



})