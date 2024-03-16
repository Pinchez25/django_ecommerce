from django.urls import path
from .views import index, product_detail, add_to_cart, shopping_cart, remove_from_cart

app_name = 'shop'
urlpatterns = [
    path('', index, name='index'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('<slug:category_slug>/', index, name='product_list_by_category'),
    path('<int:id_>/<slug:slug>/', product_detail, name='product_detail'),
    path('shopping-cart', shopping_cart, name='shopping_cart'),
    path('product/remove/', remove_from_cart, name='remove-from-cart'),
    # path('search/product-search/',  search_product, name='product-search')

]
