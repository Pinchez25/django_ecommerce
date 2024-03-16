from decimal import Decimal

from .models import Product


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket')
        if not basket:
            basket = self.session['basket'] = {}
        self.basket = basket

    def save(self):
        self.session.modified = True

    def add_to_cart(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': quantity, 'price': str(product.price)}
        else:
            self.basket[product_id]['quantity'] += quantity
        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)

        # A copy of the basket is created so that the original basket is not modified
        basket = self.basket.copy()

        # Add all the products to the basket copy
        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def remove(self, product_id: str):
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear_basket(self):
        del self.session['basket']
        self.save()

    def update(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] = quantity
            self.save()

    def reduce_item_quantity(self, product, quantity):
        product_id = str(product.id)
        self.basket[product_id]['quantity'] -= quantity

        if self.basket[product_id]['quantity'] < 1:
            del self.basket[product_id]
        self.save()
