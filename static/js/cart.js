const updateButtons = document.getElementsByClassName('update-cart')
// var na let
for ( var i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function() {
        const productId = this.dataset.product
        const action = this.dataset.action
        console.log('productId:', productId, 'action:', action)   
        
        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('User is not logged in')
        }else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...')

    var url = 'http://127.0.0.1:8000/update_item/'
    fetch(url, {
        method:"POST",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
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
