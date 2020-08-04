from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

from . utils import cookieCart, cartData
# Create your views here.


def store(request):

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     cookieData = cookieCart(request)
    #     cartItems = cookieData['cartItems']

    data = cartData(request)
    cartItems = data['cartItems']

        # items = []
        # order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        # cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'fhstore/store.html', context)


def cart(request):

    # IF USER IS LOGGED - ELSE, not logged
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    #     cookieData = cookieCart(request)
    #     cartItems = cookieData['cartItems']
    #     order = cookieData['order']
    #     items = cookieData['items']

        # cart = json.loads(request.COOKIES['cart'])
        # print('Cart:', cart)
        # items = []
        # order ={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        # cartItems = order['get_cart_items']

        # # COMMENT THIS AND TRY WITHOUT THIS CODE (REFRESH CART)
        # for i in cart:
        #     cartItems += cart[i]['quantity']

        #     product = Product.objects.get(id=i)
        #     total = (product.price * cart[i]['quantity'])
        #     order['get_cart_total'] += total
        #     order['get_cart_total'] += cart[i]['quantity']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'fhstore/cart.html', context)


def checkout(request):
    
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     cookieData = cookieCart(request)
    #     cartItems = cookieData['cartItems']
    #     order = cookieData['order']
    #     items = cookieData['items']

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

        # items = []
        # order ={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        # cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'fhstore/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    ProductId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', ProductId)

    customer = request.user.customer
    product = Product.objects.get(id=ProductId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.load(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # DELETE THIS? 129 +6
        total = float(data['form']['total'])
        order_transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        # DODAĆ POZA PĘTLE? PONAD RETURN? 137+8
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in')

        print('COOKIES:', request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']
        cookieData = cookieCart(request)
        items = cookieData['items']
        customer, created = Customer.objects.get_or_create(
            email = email,
            )
        customer.name = name 
        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
            )
        for item in items:
            product = Product.objects.get(id=item['product']['id'])

            orderItem = orderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )

    total = float(data['form']['total'])
    order_transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    return JsonResponse('Payment complete', safe=False)

def contact(request):
    return render(request, 'fhstore/contact.html')

def paymentInfo(request):
    return render(request, 'fhstore/payment.html')