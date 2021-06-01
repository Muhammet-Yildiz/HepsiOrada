$(function() {
    var formicon1 = $(".icon1")
    var formicon2 = $(".fa-eye")
    var formicon3 = $(".fa-eye-slash")
    var formicon4 = $(".icon4")
    var formbutton = $("#registerBtn")

    var emailInput = $("#id_email")
    var usernameInput = $("#id_username")
    var passwordInput = $("#id_password")




    emailInput.attr("required", false)
    passwordInput.attr("required", false)
    usernameInput.attr("required", false)


    emailInput.attr("placeholder", "E-posta adresi")
    usernameInput.attr("placeholder", "Kullanıcı adı")
    passwordInput.attr("placeholder", "Şifre")

    emailInput.after("<small>   </small>")
    passwordInput.after("<small>  </small>")
    usernameInput.after("<small>  </small>")



    $(".form-control").removeClass("form-control")


    usernameInput.on("blur", function() {


        var usernamevalue = $(this).val()

        if (usernamevalue.length < 2) {

            if (usernamevalue.length == 0) {
                $(this).next().html("Kullanıcı adı girmelisiniz. ")


            } else {
                $(this).next().html("En az 2 karakter girmelisiniz. ")


            }

            formicon1.css({
                'visibility': 'visible'
            })
            $(this).css({
                'color': 'red !important',
                'background-color': 'rgba(250, 60, 60,0.1) ',
                'border': '2px solid rgb(251, 111, 111)',

            })
            $(this).addClass("danger")



            formicon4.css({
                'bottom': '122px',
            })

            formicon2.css({
                'bottom': '35px',
            })
        } else {


            $(this).css({
                'background-color': 'white ',
                'border': '#ccc solid 2px '
            })
            formicon1.css({
                'visibility': 'hidden'
            })
            $(this).next().html("")
            $(this).removeClass("danger")



            formicon2.css({
                'bottom': '35px',
            })


            formicon4.css({
                'bottom': '148px',
            })

        }

    })



    var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;

    emailInput.on("blur", function() {


        var emailvalue = $(this).val()

        durum = testEmail.test(emailvalue)

        console.log(emailvalue, durum)

        if (durum == true) {
            $(this).css({
                'background-color': 'white ',
                'border': '#ccc solid 2px '
            })

            formicon4.css({
                'visibility': 'hidden'
            })
            $(this).removeClass("danger")

            $(this).next().html(" ")



            formicon2.css({
                'bottom': '55px',
            })




        } else {
            $(this).css({
                'border': '2px solid rgb(251, 111, 111)',
                'background-color': 'rgba(250, 60, 60,0.1) ',
            })
            formicon4.css({
                'visibility': 'visible',

            })

            $(this).addClass("danger")

            if ($(this).val().length == 0) {
                $(this).next().html(" ")

                $(this).after("<small>E-posta adresinizi girmelisiniz.</small>")

            } else {
                $(this).next().html(" ")

                $(this).after("<small>Geçerli bir e-posta adresi girmelisiniz.</small>")

            }


            formicon2.css({
                'bottom': '30px'
            })


        }


    })

    passwordInput.on("blur", function() {
        var passwordvalue = $(this).val()

        console.log(passwordvalue)
        console.log(passwordvalue.length)
        if (passwordvalue.length == 0) {
            $(this).css({
                'color': 'red !important',
                'background-color': 'rgba(250, 60, 60,0.1) ',
                'border': '2px solid rgb(251, 111, 111)',

            })
            $(this).addClass("danger")

            formicon2.css({
                'color': 'rgb(255, 111, 111)',

            })

            $(this).next().html("Şifre belirleyin.")


        } else {
            $(this).css({
                'background-color': '#eee',
                'border': '#ccc solid 2px '

            })

            $(this).removeClass("danger")
            formicon2.css({
                'color': 'rgb(160, 159, 159)'

            })
            $(this).next().html(" ")


        }
    })



    formicon2.on("click", function() {

        if (passwordInput.attr("type") == 'password') {
            passwordInput.attr("type", "text")
            $(this).addClass("fa-eye-slash")
            $(this).removeClass("fa-eye")

        } else {
            passwordInput.attr("type", "password")
            $(this).removeClass("fa-eye-slash")
            $(this).addClass("fa-eye")
        }

    })



    formbutton.click(function() {


        var emailvalue = emailInput.val()

        durumemail = testEmail.test(emailvalue)


        if (durumemail == false) {

            $(emailInput).css({
                'border': '2px solid rgb(251, 111, 111)',
                'background-color': 'rgba(250, 60, 60,0.1) ',
            })
            formicon4.css({
                'visibility': 'visible',

            })

            $(emailInput).addClass("danger")

            if ($(emailInput).val().length == 0) {
                $(emailInput).next().html(" ")

                $(emailInput).after("<small>E-posta adresinizi girmelisiniz.</small>")

            } else {
                $(emailInput).next().html(" ")

                $(emailInput).after("<small>Geçerli bir e-posta adresi girmelisiniz.</small>")

            }

            formicon2.css({
                'bottom': '30px'
            })


        }


        var usernamelength = usernameInput.val().length

        if (usernamelength == 0) {

            var usernamevalue = $(this).val()

            if (usernamevalue.length < 2) {
                if (usernamevalue.length == 0) {
                    $(usernameInput).next().html("Kullanıcı adı girmelisiniz. ")

                } else {
                    $(usernameInput).next().html("En az 2 karakter girmelisiniz. ")

                }
                formicon1.css({
                    'visibility': 'visible'
                })
                $(usernameInput).css({
                    'color': 'red !important',
                    'background-color': 'rgba(250, 60, 60,0.1) ',
                    'border': '2px solid rgb(251, 111, 111)',

                })
                $(usernameInput).addClass("danger")



                formicon4.css({
                    'bottom': '122px',
                })

                formicon2.css({
                    'bottom': '35px',
                })
            }

        }




        var passwordlength = passwordInput.val().length


        if (passwordlength == 0) {

            $(passwordInput).css({
                'color': 'red !important',
                'background-color': 'rgba(250, 60, 60,0.1) ',
                'border': '2px solid rgb(251, 111, 111)',

            })
            $(passwordInput).addClass("danger")

            formicon2.css({
                'color': 'rgb(255, 111, 111)',
                'bottom': '10px'
            })

            $(passwordInput).next().html("Şifre belirleyin.")

        }


        if (usernamelength != 0 && passwordlength != 0 && durumemail == true) {

            formbutton.attr("type", "submit")

        } else {

            formbutton.attr("type", "button")

        }
    })




})