var updateButtons = document.getElementsByClassName('update-cart')
// var na let
for ( var i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)   
        console.log('USER:', user)

        if (user == "AnonymousUser") {
            addCookieItem(productId, action)
        }else {
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('User is not authenticated')

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = {'quantity':1}
        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0) {
            console.log('Remove Item')
            delete cart[productId]
        } 
    
    }
    console.log('CART:',cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...')
    // sprobowac bez http
    var url = '/update_item/'
    fetch(url, {
        method:"POST",
        headers:{
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
        return response.json()
    // CODE BELOW DONT SHOW ERRORS BUT IT STILL NOT WORKING 
    //     return response.text()
    // .then(text => console.log(text))
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}


