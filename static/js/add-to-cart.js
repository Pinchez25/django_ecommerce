const addToCart = () => {
    const btnAddToCart = Array.from(document.getElementsByClassName('btnAddToCart'))
    const product_quantity = document.getElementById('item-quantity');
    //console.log(cartTotal.innerHTML==="41")
    btnAddToCart.forEach(btn => {
        btn.setAttribute('data-id','{{ product.id }}');
        btn.addEventListener('click', e => {
            e.preventDefault()
            let product_id = e.target.dataset.id
            let quantity;
            //$(e.target).text('Adding...')

            if(product_quantity !== undefined){
                quantity = product_quantity.value;
            }else{
                quantity = 1
            }

            $("#cart-total").innerHTML = ""
            $.ajax({
                url: "{% url 'shop:add_to_cart' %}",
                method: "POST",
                data: {
                    product_id: product_id,
                    quantity: quantity,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function (response) {
                    $("#cart-total").text(response.total_items)
                },
                error: function (error) {
                    console.log(error)
                }
            })


        })
    })
}




