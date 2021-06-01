$(function() {


    label = $("form label ")
    label.each(function(index, element) {

        value = $(element).text()

        value = value.replace(":", " ")
        $(element).text(value)
    })


    $("label[for ='id_city']").prepend(" <span> <div >  02 Adres Bilgileriniz   </div></span> ")


    $(".close_side , .giveupBtn").click(function() {
        $(".sideBar").css({
            'right': '-540px',
            'box-shadow': 'none'
        })
    })




    $(" .newAddAddres , .edit , .addAddressLink , .noaddressEmp").click(function() {
        $(".sideBar").css({
            'right': '0',
            'box-shadow': ' 0 0 100px 10000px rgba(0, 0, 0, 0.7)'

        })

    })



    $(".delete").click(function(e) {

            e.preventDefault()

            shippingId = $(this).data("id")
            process = $(this).data("process")
            $.ajax({
                method: "POST",
                url: '/addressDelete/',
                data: {
                    'shippingId': shippingId,
                    'process': process,
                    csrfmiddlewaretoken: $("input[name = csrfmiddlewaretoken]").val()
                },
                beforeSend: function() {
                    console.log("edit yada delete butonuna basmadan once")

                },
                success: function(data) {}


            })

            $(this).parent().parent().slideUp("slow")

        })
        // ------------------------------------------
        // ------------------------------------------

    $(".edit ,.newAddAddres ").click(function(e) {
        e.preventDefault()
        shippingId = $(this).data("id")
        process = $(this).data("process")

        $.ajax({
            method: "GET",
            url: '/teslimat-adreslerim/',
            data: {
                'shippingId': shippingId,
                'process': process,
                csrfmiddlewaretoken: $("input[name = csrfmiddlewaretoken]").val()
            },
            beforeSend: function() {},
            success: function(data) {

                ilkForm = $(data).find(".sideBar form ")[0]

                $(ilkForm).find("label[for ='id_city']").prepend(" <span> <div >  02 Adres Bilgileriniz   </div></span> ")

                $(".sideBar form ").html(ilkForm)

                $(".saveBtn").attr("data-id", shippingId)

                label = $(ilkForm).find("form label ")
                label.each(function(index, element) {

                    value = $(element).text()
                    value = value.replace(":", " ")
                    $(element).text(value)
                })



            }


        })





    })




})