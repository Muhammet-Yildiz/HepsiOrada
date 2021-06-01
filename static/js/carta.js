var updateBtns = document.getElementsByClassName('update-cart')

var icons = $(".product-quantity i  , .trushSvg")

$(icons).click(function() {
    var action = $(this).data("action")
    var productId = $(this).data("product")

    var chooseColor = $(this).parent().parent().find(".product-choose .chooseColor ").html()
    var chooseSize = $(this).parent().parent().find(".product-choose .chooseSize ").html()

    if (chooseColor == "None" || chooseColor == undefined) {
        chooseColor = null
    } else {
        chooseColor = chooseColor.trim()

    }

    if (chooseSize == "None" || chooseSize == undefined) {
        chooseSize = null
    } else {
        chooseSize = chooseSize.trim()

    }



    if (user == 'AnonymousUser') {

        addCookieItem(productId, action, chooseColor, chooseSize)

    } else {
        quantityUpdate(productId, action, chooseColor, chooseSize)

    }
})


function quantityUpdate(productId, action, chooseColor, chooseSize) {

    var url = '/store/update_item/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action,
                'chooseSize': chooseSize,
                'chooseColor': chooseColor,

            })

        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            location.reload()
        })


}






for (i = 0; i < updateBtns.length; i++) {

    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product

        var action = this.dataset.action

        var chooseSize = $(".size_opts .Select").html()

        var chooseColor = $(".color .colorChoose").parent().data("color")

        if (chooseColor == undefined) {

            var chooseColor = $(this).data("color")

            if (chooseColor == "None" || chooseColor == undefined) {
                chooseColor = null

            }


        }
        if (chooseSize == undefined) {
            var chooseSize = $(this).data("size")
            if (chooseSize == "None" || chooseSize == undefined) {

                chooseSize = null
            }

        }


        if (user == 'AnonymousUser') {

            tıklanan = $(this)
            button = $(tıklanan)[0]

            if (window.location.pathname == "/") {


                chooseColor = $(button).data("color")
                chooseSize = $(button).data("size")


            } else {

                var chooseSize = $(".size_opts .Select").html()
                var chooseColor = $(".color .colorChoose").parent().data("color")


            }



            addCookieItem(productId, action, chooseColor, chooseSize)



        } else {

            updateUserOrder(productId, action, chooseColor, chooseSize)

        }

    })

}

function updateUserOrder(productId, action, chooseColor, chooseSize) {

    var url = '/store/update_item/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action,
                'chooseColor': chooseColor,
                'chooseSize': chooseSize,

            })

        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            addalert()
        })



}


function addCookieItem(productId, action, chooseColor, chooseSize) {

    if (chooseColor == "None" || chooseColor == undefined) {
        chooseColor = null

    }

    if (chooseSize == "None" || chooseSize == undefined) {
        chooseSize = null

    }



    if (action == 'add') {

        if (cart[productId + "-" + chooseColor + "-" + chooseSize] == undefined) {
            cart[productId + "-" + chooseColor + "-" + chooseSize] = { 'quantity': 1, 'color': chooseColor, 'size': chooseSize, 'productId': productId }
        } else {
            cart[productId + "-" + chooseColor + "-" + chooseSize]['quantity'] += 1
        }
    }


    if (action == 'remove') {

        cart[productId + "-" + chooseColor + "-" + chooseSize]['quantity'] -= 1


        if (cart[productId + "-" + chooseColor + "-" + chooseSize]['quantity'] <= 0) {

            delete cart[productId + "-" + chooseColor + "-" + chooseSize]

        }

    }

    if (action == 'allremove') {

        cart[productId + "-" + chooseColor + "-" + chooseSize]['quantity'] = 0

        if (cart[productId + "-" + chooseColor + "-" + chooseSize]['quantity'] <= 0) {

            delete cart[productId + "-" + chooseColor + "-" + chooseSize]

        }

    }




    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'

    konum = window.location.pathname
    if (konum == '/store/sepetim/') {
        location.reload()
    }


    addalert()



}


$(function() {



    $(".add-btn").click(function() {

        if (window.location.pathname == "/store/sepetim/") {
            location.reload()

        }

    })





})

function addalert() {
    alert1 = $(".addproductAlert")
    alert2 = $(".addproductAlert2")
    alert3 = $(".addproductAlert3")
    alert4 = $(".addproductAlert4")


    if (alert1.css('display') == 'none') {
        if (alert4.css('display') == 'flex') {
            alert4.animate({
                'top': '95px'
            }, 400)

            if (alert3.css('display') == 'flex') {
                alert3.animate({
                    'top': '155px'
                }, 400)


                if (alert2.css('display') == 'flex') {
                    alert2.animate({
                        'top': '215px'
                    }, 400)


                }



            }
        }

        alert1.css({
            'display': 'flex ',
        })

        alert1.animate({
            'right': '35px',
        }, 400)


        setTimeout(function() {
            alert1.css({
                'display': 'none',
                'right': '-120px',
                'top': '25px '
            })
        }, 2700)

    } else if (alert2.css('display') == 'none') {

        if (alert1.css('display') == 'flex') {
            alert1.animate({
                'top': '95px'
            }, 400)

            if (alert4.css('display') == 'flex') {
                alert4.animate({
                    'top': '155px'
                }, 400)



                if (alert3.css('display') == 'flex') {
                    alert3.animate({
                        'top': '215px'
                    }, 400)


                }


            }

        }


        alert2.css({
            'display': 'flex',
        })

        alert2.animate({
            'right': '35px'
        }, 400)
        setTimeout(function() {
            alert2.css({
                'display': 'none',
                'right': '-120px',
                'top': '25px '

            })
        }, 2700)


    } else if (alert3.css('display') == 'none') {

        if (alert2.css('display') == 'flex') {

            alert2.animate({
                'top': '95px'
            }, 400)

            if (alert1.css('display') == 'flex') {

                alert1.animate({
                    'top': '155px'
                }, 400)

                if (alert4.css('display') == 'flex') {
                    alert4.animate({
                        'top': '215px'
                    }, 400)


                }


            }


        }

        alert3.css({
            'display': 'flex',
        })
        alert3.animate({
            'right': '35px'
        }, 400)
        setTimeout(function() {
            alert3.css({
                'display': 'none',
                'right': '-120px',
                'top': '25px '

            })
        }, 2700)

    } else if (alert4.css('display') == 'none') {

        if (alert3.css('display') == 'flex') {
            alert3.animate({
                'top': '95px'
            }, 400)

            if (alert2.css('display') == 'flex') {

                alert1.animate({
                    'top': '155px'
                }, 400)


                if (alert1.css('display') == 'flex') {
                    alert1.animate({
                        'top': '215px'
                    }, 400)


                }



            }
        }

        alert4.css({
            'display': 'flex',
        })
        alert4.animate({
            'right': '35px'
        }, 400)
        setTimeout(function() {
            alert4.css({
                'display': 'none',
                'right': '-120px',
                'top': '25px '

            })
        }, 2700)

    }



}