$(function() {

    var emailInput = $("#id_email")
    var passwordInput = $("#id_password")
    var formbutton = $("#continueBtn")
    var formicon1 = $(".fa-exclamation-triangle")
    var formicon7 = $(".fa-times ")
    emailInput.after("<small>   </small>")

    emailInput.removeClass("form-control")

    emailInput.attr("required", false)

    emailInput.attr("placeholder", "E-posta adresi")

    passwordInput.attr("placeholder", "Şifre")

    var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;

    emailInput.focus(function() {
        formicon1.css('display', 'none')
    })

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


            formicon1.css('display', 'none')


            formbutton.css({

                'background-color': '#FF6000'
            })


        } else {
            $(this).css({
                'border': '2px solid rgb(251, 111, 111)',
                'background-color': 'rgba(250, 60, 60,0.1) ',
            })
            formicon1.css({
                'visibility': 'visible'
            })

            $(this).addClass("danger")

            // email adresinizi girin uyarısı ıcın 
            if ($(this).val().length == 0) {
                $(this).next().html(" ")

                $(this).after("<small>E-posta adresinizi girmelisiniz.</small>")

            } else {
                $(this).next().html(" ")

                $(this).after("<small>Geçerli bir e-posta adresi girmelisiniz.</small>")

            }
            formicon1.css({
                'display': 'inline',
                'color': ' red '
            })



        }


    })



    formbutton.click(function() {



        var emailvalue = emailInput.val()

        durumemail = testEmail.test(emailvalue)


        if (durumemail == true) {

            var url = '/hasuseremail/'

            fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify({
                        'emailvalue': emailvalue,
                    })

                })
                .then((response) => {
                    return response.json()
                })
                .then((data) => {
                    if (data.data) {

                        formbutton.attr("type", "submit")

                        $(".form2").submit()

                    } else {
                        formbutton.attr("type", "button")

                        setTimeout(function() {

                            $(".emailerror").css('display', 'inline-block')

                        }, 1800)

                        formicon7.click(function() {
                            $(".emailerror").css('display', 'none')


                        })


                    }
                })




        } else {

            formbutton.attr("type", "button")

        }
    })




})