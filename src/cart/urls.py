from django.urls import path
from . import views
#from D_P.src.cart.models import Payment

app_name = 'cart'
urlpatterns = [
    path('', views.CartView.as_view(), name='summary'),
    path('shop/', views.ProductListView.as_view(), name='product_list'),
    path('shop/<slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('increase-quantity/<pk>/', views.IncreaseQuantityView.as_view(), name='increase-quantity'),
    path('decrease-quantity/<pk>/', views.DecreaseQuantityView.as_view(), name='decrease-quantity'),
    path('remove-from-cart/<pk>/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('payment/', views.PaymentView.as_view(),name='payment'),
    path('thank-you/', views.ThankYouView.as_view(),name='thank-you'),
    path('confirm-order/', views.ConfirmOrderView.as_view(),name='confirm-order')
    
]
