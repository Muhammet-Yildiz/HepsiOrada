$(function() {

    var icon = $(".fa-chevron-down")
    $(".order_top").click(function() {

        var icon1 = $(this).find(icon)

        $(this).next().slideToggle(450)

        if (icon1.hasClass("fa-chevron-down")) {
            icon1.removeClass("fa-chevron-down")

            icon1.addClass("fa-times")
        } else {
            icon1.addClass("fa-chevron-down")

            icon1.removeClass("fa-times")
        }




    })



})