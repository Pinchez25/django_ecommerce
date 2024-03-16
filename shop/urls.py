from django.urls import path
from .views import index, product_detail, add_to_cart, shopping_cart, remove_from_cart, create_checkout_session
from django.views.generic import TemplateView

app_name = 'shop'
urlpatterns = [
    path('', index, name='index'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('<slug:category_slug>/', index, name='product_list_by_category'),
    path('<int:id_>/<slug:slug>/', product_detail, name='product_detail'),
    path('shopping-cart', shopping_cart, name='shopping_cart'),
    path('product/remove/', remove_from_cart, name='remove-from-cart'),
    # path('search/product-search/',  search_product, name='product-search')
    path('cancel-checkout/stop-checkout/', TemplateView.as_view(template_name='cancel.html'), name='cancel-checkout'),
    # path('shop/checkout/', TemplateView.as_view(template_name='checkout.html'), name='checkout'),
    path('checkout/success/checkout-successful', TemplateView.as_view(template_name='success.html'),
         name='checkout-success'),
    path('checkout/session/create/', create_checkout_session, name='create-checkout-session'),

]
