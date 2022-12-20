if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
}
else {
    ready()
}

function ready() {
    console.log('ready')
    var uniq = 'id' + (new Date()).getTime();
    console.log(uniq)
    var cartRemoveButtons = document.getElementsByClassName('btn-danger')
    for (var i = 0; i < cartRemoveButtons.length; i++) {
        var button = cartRemoveButtons[i]
        button.addEventListener('click', removeCartItem)
    }

    var quantityInputs = document.getElementsByClassName('cart-quantity-input')
    for (var i = 0; i < quantityInputs.length; i++) {
        var input = quantityInputs[i]
        input.addEventListener('change', quantityChanged)
    }

    var clearCart = document.getElementById('clearCart')
    if (clearCart != null) {
        clearCart.addEventListener('click', clearCartClicked)
    }

    var addToCart = document.getElementById('addToCart')
    if (addToCart != null) {
        addToCart.addEventListener('click', addToCartClicked)
    }
    var cartCount = document.getElementById('cart-count')


    function getTotalItems() {
        cart = JSON.parse(localStorage.getItem('cart'))
        var totalItems = 0
        for (var i = 0; i < cart.products.length; i++) {
            totalItems += parseInt(cart.products[i].quantity)
        }
        console.log(totalItems)
        document.getElementsByClassName('cart-count')[0].innerHTML = `${totalItems}`;

    }


    function addToCartClicked(event) {
        var button = document.getElementById('addToCart');
        var productId = button.getAttribute('data-pid')
        var name = button.getAttribute('data-name')
        var price = button.getAttribute('data-price')

        // try to get cart    
        cart = JSON.parse(localStorage.getItem('cart'))
        // if cart is present
        if (cart != null) {
            productList = cart.products
            for (var i = 0; i < productList.length; i++) {

                if (productList[i].id === productId) {
                    productList[i].quantity += 1
                    localStorage.setItem('cart', JSON.stringify(cart))
                    return
                }
            }
            var newItem = {
                'id': productId,
                'name': name,
                'price': price,
                'quantity': 1
            }
            productList.push(newItem)
            localStorage.setItem('cart', JSON.stringify(cart))
            getTotalItems()
        } else {
            cart = {
                'cartId': uniq,
                'products': [
                    {
                        'id': productId,
                        'name': name,
                        'price': price,
                        'quantity': 1
                    }
                ]
            }
            localStorage.setItem('cart', JSON.stringify(cart))
            getTotalItems()
        }

        getTotalItems()
    }



    function getProducts() {
        var cartItems = document.getElementsByClassName('cart-items')[0]
        cart = JSON.parse(localStorage.getItem('cart'))
        for (i = 0; i <= cart.products.length; i++) {
            var cartRow = document.createElement('tr')

            cartRow.className = "cart-row";

            var cartRowContent = `<td class="cart-item cart-column">
            <span class="cart-item-title"> ${cart.products[i].name} </span>
            </td>
            <td></td>
            <td class="cart-price cart-column"5>${cart.products[i].price}</td>
            <td class="cart-quantity cart-column">
                <input class="cart-quantity-input" type="number" value=${cart.products[i].quantity}>
            </td>
            <td>
                <button class="btn btn-danger" type="button">REMOVE</button>
            </td>
            `
            cartRow.innerHTML = cartRowContent
            cartItems.append(cartRow)
            cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
            cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)

            updateCartTotal()
        }

    }
    getProducts()


function clearCartClicked() {

        var cartItems = document.getElementsByClassName('cart-items')[0]
        while (cartItems.hasChildNodes()) {
            cartItems.removeChild(cartItems.firstChild)
        }
        localStorage.removeItem('cart');
        updateCartTotal()
    }



    function quantityChanged(event) {
        var input = event.target
        console.log(input.value)
        if (isNaN(input.value) || input.value <= 0) {
            input.value = 1
        }
        updateCartTotal()
    }

    function removeCartItem(event) {
        var buttonClicked = event.target
        buttonClicked.parentElement.parentElement.remove()
        updateCartTotal()
    }


    function updateCartTotal() {
        var cartItemContainer = document.getElementsByClassName('cart-items')[0]
        var cartRows = cartItemContainer.getElementsByClassName('cart-row')


        var total = 55
        for (var i = 0; i < cartRows.length; i++) {
            var cartRow = cartRows[i]
            var priceElement = cartRow.getElementsByClassName('cart-price')[0]
            var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
            var price = parseFloat(priceElement.innerText.replace('$', ''))
            var quantity = quantityElement.value
            total = total + (price * quantity)
        }
        total = Math.round(total * 100) / 100
        console.log(total)
        document.getElementsByClassName('cart-total-price')[0].innerText = '$' + total
    }

}
updateCartTotal()