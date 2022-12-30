from decimal import Decimal

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .cart import Basket
from .forms import AddToCartForm
from .models import Category, Product


# Create your views here.
def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    search_query = ''
    if request.GET.get('search_product'):
        search_query = request.GET.get('search_product')
        products = products.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
        )

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/index.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'query':search_query
    })


def product_detail(request, id_, slug):
    product = get_object_or_404(Product, id=id_, slug=slug, available=True)
    form = AddToCartForm()

    # if not form.is_valid():
    #     return form.errors

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'form': form,
    })


def add_to_cart(request):
    basket = Basket(request)
    if request.method == "POST":
        action = request.POST.get('action')
        product_id = int(request.POST.get("product_id"))
        quantity = int(request.POST.get("quantity"))
        product = get_object_or_404(Product, id=product_id)

        if action == "add":
            basket.add_to_cart(product, quantity)
            cart_prod = basket.basket.get(str(product_id))
            # print(basket.basket)
            return JsonResponse({
                "message": "Product Successfully Added to Cart",
                'total_items': basket.__len__(),
                'cart_total': basket.get_total_price(),
                'sub_total': cart_prod['quantity'] * Decimal(cart_prod['price']),
            })
        elif action == "reduce":
            basket.reduce_item_quantity(product, quantity)
            cart_prod = basket.basket.get(str(product_id))

            if cart_prod is not None:
                subtotal = cart_prod['quantity'] * Decimal(cart_prod['price'])
                return JsonResponse({
                    "total_items": basket.__len__(),
                    'cart_total': basket.get_total_price(),
                    'sub_total': subtotal,
                })
            else:
                basket.remove(str(product.id))

                return JsonResponse({
                    'msg': "Item no Longer in cart",
                    'total_items': basket.__len__(),
                    'cart_total': basket.get_total_price(),
                })
    else:
        return JsonResponse({
            "message": "Unknown action"
        })


def shopping_cart(request):
    return render(request, 'shop/cart.html')


def remove_from_cart(request):
    basket = Basket(request)

    if request.method == "POST":
        product_id = request.POST.get('product')

        if product_id is not None:
            basket.remove(product_id)
            return JsonResponse({
                'message': "Product successfully removed from cart",
                'total_items': basket.__len__(),
                'cart_total': basket.get_total_price(),

            })

        else:
            print("Undefined product id")

# def search_product(request):
#     if request.method == "GET":
#         print(request.GET)
#
#     return JsonResponse({
#         'message': f'You searched for'
#     })
