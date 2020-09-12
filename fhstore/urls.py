from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    # path('payment/', views.paymentInfo, name='payment_info'),
    # path('contact/', views.contact, name='contact'),
    #CRM urls
    path('crm_order/', views.crmOrder, name='crm_order'),
    path('crm_product/', views.crmProduct, name='crm_product'),
    path('crm/', views.crmHome, name='crm_home'),
]
