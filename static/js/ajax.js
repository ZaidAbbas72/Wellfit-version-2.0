$(document).ready(function () {
    var classForm = $(".class_form")
    classForm.submit(function (event) {
        event.preventDefault();
        var thisForm = $(this)
        var actionEndpoint = thisForm.attr("data-endpoint");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,

            success: function (data) {
                var submitForm = thisForm.find(".submit-span");
                if (data.added) {
                    submitForm.html("<input type='submit' value='Cancel' class='input' />")
                } else if (!data.added) {
                    submitForm.html("<input type='submit' value='Register' class='input' />")
                }
                var cartCount = $(".cart")
                cartCount.text(data.cartItemCount)

                var currentPath = window.location.href
                if (currentPath.indexOf("profile") != -1) {
                    refreshRegisters()
                }
            },

            error: function (errorData) {
                alert("An error occurred")
                location.reload();
            }
        })
    })


    function refreshRegisters() {
        var registersTable = $(".registers-table")
        var registersBody = registersTable.find(".registers-body")
        var classRows = registersBody.find(".registered-class")
        var currentPath = window.location.href
        var refreshRegisterUrl = 'api/profile';
        var refreshRegisterMethod = "GET";
        var data = {};

        $.ajax({
            url: refreshRegisterUrl,
            method: refreshRegisterMethod,
            data: data,

            success: function (data) {
                var hiddenCartItemRemoveForm = $(".cart-item-remove-form")

                if (data.classes.length > 0) {
                    classRows.html(" ")
                    i = data.classes.length
                    var classes = data.classes.reverse();
                    $.each(data.classes, function (index, value) {
                        location.reload();
                        var newCartItemRemove = hiddenCartItemRemoveForm.clone()
                        newCartItemRemove.find(".cart-item-class-id").val(value.id)
                        registersBody.prepend("<tr>\
                                            <th scope=\"row\">" + i + "</th>\
                                            <td>" + value.title + "</td>\
                                            <td>" + value.price + "</td>\
                                            <td class=\"buttons\">" + newCartItemRemove.html() + "<a class=\"detail\" href=\"{% url 'class_details' class.id %}\">View Details</a>" + "</td>\
                                            </tr>")
                        i--
                    })
                    registersBody.find(".subtotal").text(data.subtotal)
                    registersBody.find(".total").text(data.total)

                } else {
                    window.location.href = currentPath
                }
            },
            error: function (errorData) {
                alert("An error occurred")
            }
        })
    }
})
