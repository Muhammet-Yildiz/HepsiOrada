$(function() {

    var StarEmp = $(".Ratings_star ")
    var Star = $(".Ratings_star i ")

    $(Star).on("mouseover ", function(e) {

        hoverlanan = $(this)
        hoverindex = $(this).data("rate")

        secilen = $(".Ratings_star i.checked ")

        Star.each(function(index, element) {
            $(secilen).removeClass("checked")

            if (index < hoverindex) {

                $(element).addClass("check")

            } else {

                $(element).removeClass("check")
            }

        })


    })


    $(StarEmp).mouseleave(function() {
        secilen = $(".Ratings_star i.checked ")
        if (secilen != undefined) {
            $(secilen).addClass("checked")
        }


        Star.each(function(index, element) {
            $(element).removeClass("check")

        })




    })


    $(Star).click(function() {

        tıklanan = $(this)
        tıklananndex = $(this).data("rate")

        Star.each(function(index, element) {
            $(element).removeClass("check")

            if (index < tıklananndex) {

                $(element).addClass("checked")

            } else {
                $(element).removeClass("checked")

            }

        })



    })


    $(".commentBtn").on("click", function(e) {

        e.preventDefault()
        _productid = $(".commentBtn").data("productid")
        içerik = $(".commentBtn").parent().find("#comment_content")[0]
        _star = $(".commentBtn").parent().find(".Ratings_star i.checked")

        $.ajax({

            method: "POST",
            url: $(this).parent().attr("action"),
            data: {
                'içerik': $(içerik).val(),
                'star': $(_star).length,
                'productid': _productid,
                csrfmiddlewaretoken: $("input[name = csrfmiddlewaretoken]").val()

            },
            beforeSend: function() {},
            success: function(data) {
                alert1 = $(".getcommentalert")
                alert1.css('display', 'flex')
                $(".side_wrapper").html(alert1)


            }

        })


    })


    $("#comment_content").blur(function() {

        console.log($(this).val().length)
        if ($(this).val().length != 0) {
            $(this).css({
                'border': '#ccc solid 2px  ',
                'background-color': 'white'
            })

        } else {
            $(this).css({
                'border': '#eee solid 2px  ',
                'background-color': '#eee'
            })
        }

    })




    $(".close_side").click(function() {

        $(".right_sidebar").css({
            'right': '-540px',
            'box-shadow': 'none'
        })


    })

    $(".evaluateBtn").click(function(e) {
        e.preventDefault()
        _productid = $(this).data("id")
        $.ajax({
            method: "POST",
            url: '/evaluate/',
            data: {
                'productid': _productid,
                csrfmiddlewaretoken: $("input[name = csrfmiddlewaretoken]").val()
            },
            beforeSend: function() {},
            success: function(data) {
                if (data.data == false) {

                    if (data.again == true) {
                        alert("Bu urunu kullanıcı daha once degerlendırmıs .Tekrar degerlendıremez")
                    } else {
                        $(".alert_dngrcmt").css({
                            'visibility': 'visible'
                        })
                        setTimeout(function() {
                            $(".alert_dngrcmt").css({
                                'visibility': 'hidden'
                            })
                        }, 8500)

                    }

                } else {
                    if (data.productColor == null) {

                        $(".side_chooseColor").parent().html(" ")

                    } else {
                        $(".side_chooseColor").html(data.productColor)

                    }

                    if (data.productSize == null) {
                        $(".side_chooseSize").parent().html(" ")

                    } else {
                        $(".side_chooseSize").html(data.productSize)

                    }


                    $(".right_sidebar").css({
                        'right': '0',
                        'box-shadow': '0 0 100px 10000px rgba(0, 0, 0, 0.7)',
                    })

                    if (window.location.pathname == "/Sipari%C5%9Flerim/") {

                        $(".mex-ProducImg img ").attr("src", data.productImgurl)
                        $(".com_title").html(data.productName)
                        $(".mex-evaluate div b").html(" -   " + data.commentNumber)
                        $(".mex-evaluate span span").html(data.averageStar)
                        $(".commentBtn").attr("data-productid", _productid)
                    }


                }


            }

        })





    })



    $(".seeCommentlink").click(function() {

        var locationHeight = $(".Comment_topInfo").position();
        window.scroll({
            top: locationHeight.top - 80,
            left: 0,
            behavior: 'smooth'
        });


    })


    averageStar = $(".averageStar").html()

    targetStar = parseInt(averageStar)
    star = $(".top_star_average i ")

    star.each(function(index, element) {
        if (index < targetStar) {

            $(element).addClass("checked")
        }
    })


    averageStarr = $(".averageStarr").html()

    targetStar = parseInt(averageStar)
    star = $(".top_star_averages i ")

    star.each(function(index, element) {
        if (index < targetStar) {

            $(element).addClass("checked")
        }
    })



    const comment = $(".comment_w")

    comment.each(function() {
        star = $(this).find(".comment_ratings i")
        AverageStar = $(this).find(".AverageStar").html()
        targetStar = parseInt(AverageStar)
        star.each(function(index, element) {
            if (index < targetStar) {

                $(element).addClass("checked")
            }
        })
    })

    $(".comment_rating_wrap i").click(function(e) {

        e.preventDefault()

        element = $(this)


        commentId = $(this).data('id')
        process = $(this).data('process')


        $.ajax({
            method: "POST",
            url: '/commentLikeDislike/',
            data: {
                'commentId': commentId,
                'process': process,
                csrfmiddlewaretoken: $("input[name = csrfmiddlewaretoken]").val()
            },
            beforeSend: function() {},
            success: function(data) {
                $(".dislike_number").html(data.dislikesayı)
                $(".like_number").html(data.likesayı)
                $(element).parent().parent().parent().html("<p class='thank'> Teşekkür ederiz </p>  ")

            }

        })

    })




})