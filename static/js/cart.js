const updateButtons = document.getElementsByClassName('update-cart')

for (i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function() {
        const productId = this.dataset.product
        const action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)   
        
        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('User is not logged in')
        } else {
            updateUserOrder(productId, action)
        }
    })
}
function updateUserOrder(productId, action) {
    console.log('User is logged in')

    const url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((resonse) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        // location.reload()
    })
}
