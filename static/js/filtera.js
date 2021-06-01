$(function() {
    $(".range2").on("change  keyup  input ", function() {
        $(".numberInput").val($(this).val())
    })
    $(".numberInput").on("input change keypress keyup", function() {
        $(".range2").val($(this).val())
    })




    var filterCheck = $(".filter-checkbox")
    $(".filter-checkbox , .FilterpriceBtn").on("click", function(e) {
        var filterObj = {}

        var _minPrice = $("#Minprice").val()

        var _maxPrice = $("#Maxprice").val()

        if (_minPrice == '') {
            var _minPrice = $("#Minprice").attr("min")
        }
        if (_maxPrice == '') {
            var _maxPrice = $("#Minprice").attr("max")

        }

        filterObj.minPrice = _minPrice
        filterObj.maxPrice = _maxPrice

        filterCheck.each(function(index, eleman) {

            filterVal = $(this).val()

            filterData = $(this).data("filter")

            filterObj[filterData] = Array.from(document.querySelectorAll('input[data-filter=' + filterData + ']:checked ')).map(function(el) {

                return el.value

            })

        })

        $.ajax({

            url: '/filter-data',
            method: "GET",
            data: filterObj,
            dataType: 'json',
            beforeSend: function() {

                $(".products-emp").html('')
                $("#transition").css({
                    'display': 'flex'
                })

            },
            success: function(res) {

                setTimeout(function() {
                    $("#transition").css({
                        'display': 'none'
                    })
                    $(".products-emp").html(res.data)
                }, 2000)


            },
            error: function() {

                $(".products-emp").html("Hata var !!! ")
                $("#transition").css({
                    'display': 'none'
                })
            }
        })


    })



    var categories = document.querySelectorAll(".cat_title")

    $(".cat-input").on("keyup paste  ", function() {

        var value = $(this).val()
        categories.forEach(function(element) {
            var parent = $(element).parent()
            var elementvalue = element.textContent.toLowerCase()
            if (elementvalue.indexOf(value) == -1) {
                parent.css("display", "none")
            } else {
                parent.css("display", "flex")
            }
        })
    })



    var brands = document.querySelectorAll(".brand_title")


    $(".brand-input").on("keyup paste  ", function() {

        var value = $(this).val()
        brands.forEach(function(element) {
            var parent = $(element).parent()
            var elementvalue = element.textContent.toLowerCase()
            if (elementvalue.indexOf(value) == -1) {
                parent.css("display", "none")
            } else {
                parent.css("display", "flex")
            }
        })
    })




})