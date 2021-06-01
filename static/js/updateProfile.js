$(function() {

    $("#div_id_password").css("display", "none")
    var usernameInput = $("#id_username")

    var emailInput = $("#id_email")
    var savebtn = $("#saveBtn")
    var birthdayInput = $("#id_birthday")
    var phoneInput = $("#id_phone")
    var usertxt = $("#hint_id_username")
    usertxt.css('display', 'none')

    emailInput.after("<small></small>")
    usernameInput.after("<small></small>")
    phoneInput.after("<small></small>")

    $("#div_id_username label").html("Kullanıcı Adı")
    $("#div_id_email label").html("E-Posta")

    $("#div_id_username ").append("<i></i>")
    $("#div_id_username i").addClass("fas fa-exclamation ")

    $("#div_id_email ").append("<i></i>")
    $("#div_id_email i").addClass("fas fa-exclamation ")

    $("#div_id_phone").append("<i></i>")
    $("#div_id_phone i").addClass("fas fa-exclamation ")

    usernameInput.blur(function() {

        if ($(this).val() == 0) {
            $(this).css({
                'border': 'red solid 2px  ',
            })
            $(this).parent().prev().css({
                'position': 'absolute ',
                'top': '47px  ',
                'color': 'rgb(241, 53, 53) '
            })

            $(this).next().html("Lütfen adınızı girin.")

            $("#div_id_username i").css('display', 'inline-block')
        } else {
            $(this).css({
                'border': 'rgb(187, 187, 187) solid 2px  ',
            })
            $(this).parent().prev().css({
                'position': 'absolute ',
                'top': '17px  ',
                'color': '#ccc'
            })

            $(this).next().html("")
            $("#div_id_username i").css('display', 'none')


        }
    })
    usernameInput.on("focus", function() {
        $(this).parent().prev().css({
            'position': 'absolute ',
            'top': '17px  ',
        })

    })

    var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;

    emailInput.blur(function() {

        var emailvalue = $(this).val();

        durum = testEmail.test(emailvalue)


        if (durum == true) {

            $(this).css({
                'border': 'rgb(187, 187, 187) solid 2px  ',
            })
            $(this).parent().prev().css({
                'position': 'absolute ',
                'top': '17px  ',
                'left': '10px ',
                'color': '#ccc'
            })

            $(this).next().html("")
            $("#div_id_email i").css('display', 'none')

        } else {
            // email gecersiz demekki
            if ($(this).val() == 0) {
                $(this).css({
                    'border': 'red solid 2px  ',
                })
                $(this).parent().prev().css({
                    'position': 'absolute ',
                    'top': '47px  ',
                    'color': 'rgb(241, 53, 53) '

                })
                $(this).next().html("")
                $(this).next().html("Lütfen e-posta adresinizi girin")
                $("#div_id_email i").css('display', 'inline-block')

            } else {
                $(this).next().html("")

                $(this).next().html("Geçerli bir email giriniz ")

            }

        }


    })
    emailInput.on("focus", function() {
        $(this).parent().prev().css({
            'position': 'absolute ',
            'top': '17px  ',
            'left': '10px '
        })

    })

    phoneInput.attr('maxlength', 11)
    var testPhone = /([0-9]{10})|(\([0-9]{3}\)\s+[0-9]{3}\-[0-9]{4})/
    phoneInput.blur(function() {

        durum = testPhone.test($(this).val())

        if (durum == true) {
            $(this).css({
                'border': 'rgb(187, 187, 187) solid 2px  ',
            })
            $(this).parent().prev().css({
                'position': 'absolute ',
                'top': '17px  ',
                'color': '#ccc'
            })

            $(this).next().html("")
            $("#div_id_phone i").css('display', 'none')



        } else {

            if ($(this).val() == 0) {

                $(this).next().html("Lütfen telefon numaranızı girin.")
                $(this).css({
                    'border': 'red solid 2px  ',
                })
                $(this).parent().prev().css({
                        'position': 'absolute ',
                        'top': '47px  ',
                        'color': 'rgb(241, 53, 53) '
                    })
                    // top: 17px;
                $("#div_id_phone i").css('display', 'inline-block')

            } else {
                $(this).next().html("Lütfen geçerli bir telefon numarası giriniz .  . .")

                $(this).css({
                    'border': 'red solid 2px  ',
                })

                $(this).parent().prev().css({
                    'position': 'absolute ',
                    'top': '17px  ',
                })

                $("#div_id_phone i").css('display', 'inline-block')

            }


        }


    })
    phoneInput.on("focus", function() {
        $(this).parent().prev().css({
            'position': 'absolute ',
            'top': '17px  ',
        })

    })
    phoneInput.on("keypress", function(e) {

        if (e.which > 47 && e.which < 58) {} else {
            e.preventDefault();
        }

    })

    birthdayInput.attr('type', 'date')



    savebtn.click(function() {

        var emailvalue = emailInput.val()

        durumemail = testEmail.test(emailvalue)


        var usernamelength = usernameInput.val().length

        durum = testPhone.test(phoneInput.val())



        if (durum == true && usernamelength != 0 && durumemail == true) {

            savebtn.attr("type", "submit")

        } else {

            savebtn.attr("type", "button")

        }
    })



})