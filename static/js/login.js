$(function() {

    var emailInput = $("#id_email")
    var passwordInput = $("#id_password")
    var formbutton = $("#loginBtn")
    var formicon1 = $(".fa-exclamation-triangle")
    var formicon2 = $(".fa-eye")
    var formicon3 = $(".fa-eye-slash")
    emailInput.after("<small>   </small>")
    passwordInput.after("<small>  </small>")

    emailInput.removeClass("form-control")
    passwordInput.removeClass("form-control")

    emailInput.attr("required", false)
    passwordInput.attr("required", false)

    emailInput.attr("placeholder", "E-posta adresi")

    passwordInput.attr("placeholder", "Şifre")
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

            formicon1.css({
                'visibility': 'hidden'
            })
            $(this).removeClass("danger")

            $(this).next().html(" ")




        } else {
            $(this).css({
                'border': '2px solid rgb(251, 111, 111)',
                'background-color': 'rgba(250, 60, 60,0.1) ',
            })
            formicon1.css({
                'visibility': 'visible'
            })

            $(this).addClass("danger")

            if ($(this).val().length == 0) {
                $(this).next().html(" ")

                $(this).after("<small>E-posta adresinizi girmelisiniz.</small>")

            } else {
                $(this).next().html(" ")

                $(this).after("<small>Geçerli bir e-posta adresi girmelisiniz.</small>")

            }

        }


    })

    passwordInput.on("blur", function() {
        var passwordvalue = $(this).val()

        if (passwordvalue.length == 0) {
            $(this).css({
                'color': 'red !important',
                'background-color': 'rgba(250, 60, 60,0.1) ',
                'border': '2px solid rgb(251, 111, 111)',

            })
            $(this).addClass("danger")

            formicon2.css({
                'color': 'rgba(251, 111, 111,0.9)',
            })


        } else {
            $(this).css({
                'background-color': '#eee',
                'border': '#ccc solid 2px '

            })

            $(this).removeClass("danger")
            formicon2.css({
                'color': 'rgb(82, 82, 82)'
            })


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


        if (emailvalue.length == 0) {

            $(emailInput).css({
                'border': '2px solid rgb(251, 111, 111)',
                'background-color': 'rgba(250, 60, 60,0.1) ',
            })
            formicon1.css({
                'visibility': 'visible'
            })

            $(emailInput).addClass("danger")

            if ($(emailInput).val().length == 0) {
                $(emailInput).next().html(" ")

                $(emailInput).after("<small>E-posta adresinizi girmelisiniz.</small>")

            } else {
                $(emailInput).next().html(" ")

                $(emailInput).after("<small>Geçerli bir e-posta adresi girmelisiniz.</small>")

            }



        }

        durumemail = testEmail.test(emailvalue)


        var passwordlength = passwordInput.val().length


        if (passwordlength == 0) {
            $(passwordInput).css({
                'color': 'red !important',
                'background-color': 'rgba(250, 60, 60,0.1) ',
                'border': '2px solid rgb(251, 111, 111)',

            })
            $(passwordInput).addClass("danger")

            formicon2.css({
                'color': 'rgba(251, 111, 111,0.9)',
            })

        }


        if (passwordlength != 0 && durumemail == true) {

            formbutton.attr("type", "submit")

        } else {

            formbutton.attr("type", "button")

        }
    })




})