$(function() {

    $(".likeBtn").click(function(e) {
        e.preventDefault();
        var iconheart = $(e.target)

        id = $(this).data("id")
        userid = $(this).data("userid")


        if (userid == "None") {
            window.location.pathname = "/customer/login"
        } else {


            $.ajax({
                url: "/addproductlike/" + id,
                method: "GET",

                success: function(data) {
                    if (iconheart.is("i")) {
                        iconheart.replaceWith("<img width='27px' src='/media/global/heart.svg'>")

                    } else if (iconheart.is("img")) {
                        iconheart.replaceWith("<i class='fas fa-heart iconheart text-orange'> </i>")
                    }
                }
            })

        }




    })


    $(".extra .firstimage").addClass("border_orange")

    $(".extra img").click(function(e) {
        clickImage = $(e.target)[0];


        hedef = $(clickImage).attr("src")

        mainImage = $(".product-img img ")[0]


        $(mainImage).attr("src", hedef)


        $(".js-image-zoom__zoomed-image").addClass("ChangeSrc")
        $('.ChangeSrc').css("background-image", "url(http://127.0.0.1:8000" + hedef + ")");


        alternatif_img = $(".extra img ")

        alternatif_img.each(function(index, element) {

            $(element).removeClass("border_orange")
        })
        $(clickImage).addClass("border_orange")

    })






    var size = $(".sizelabel")

    var ilkEleman = size[0]

    $(ilkEleman).addClass("Select")

    var selectSizeLabel = $(".choseSize")

    size.on("click", function() {

        var size = $(".sizelabel")
        var tıklanan = $(this)[0]

        size.each(function(index, eleman) {


            size = $(eleman)[0]

            $(size).removeClass("Select")

            $(tıklanan).addClass("Select")
            selectSizeLabel.html($(tıklanan).html())
        })

    })


    var color = $(".color")

    var firstelement = color[0]

    if ($(firstelement).data("color") == "beyaz") {
        $(firstelement).find("i").css("color", "black")
    }
    $(firstelement).find(".select_color").css("display", "inline-block")
    $(firstelement).find(".select_color").addClass("colorChoose")



    color.on("click", function(e) {

        var color = $(".color")
        var tıklanan = $(this)[0]

        if ($(tıklanan).css("background-color") == "rgb(255, 255, 255)") {
            $(tıklanan).find("i").css("color", "black")
        }


        color.each(function(index, eleman) {

            color = $(eleman)[0]

            $(color).find(".select_color").css("display", "none")

            $(color).find(".select_color").removeClass("colorChoose")


        })

        $(tıklanan).find(".select_color").css("display", "inline-block")
        $(tıklanan).find(".select_color").addClass("colorChoose")

    })


})