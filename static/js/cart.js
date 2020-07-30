
const updateButtons = document.getElementsByClassName('update-cart')

for (i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function() {
        const productId = this.dataset.product
        const action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)        
    })
}