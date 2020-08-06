from django.shortcuts import render
from django.http import JsonResponse

from .models import *

import json
import datetime

def cookieCart(request):

# BELOW ELSE 
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:',cart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

    for i in cart:
        cartItems += cart[i]['quantity']
        product = Product.objects.get(id=i)
        total = (product.price * cart[i]['quantity'])
        order['get_cart_total'] += total
        order['get_cart_items'] += cart[i]['quantity']

        item = {
            'product': {
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'imageURL':product.imageURL,
                },
            'quantity': cart[i]['quantity'],
            'get_total': total,
        }
        items.append(item)

        if product.digital == False:
            order['shipping'] = True

    return {'cartItems':cartItems, 'order':order, 'items':items}

# SHORTCUT FUNCTION FOR VIEWS.PY - store, checkout, cart
def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems':cartItems, 'order':order, 'items':items}