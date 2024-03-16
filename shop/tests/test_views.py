from django.test import TestCase, Client
from django.urls import reverse
from ..models import Category, Product


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            category=self.category,
            price=10.00,
            available=True
        )

    def test_index_view(self):
        url = reverse('shop:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/index.html')

    def test_product_list_by_category_view(self):
        url = reverse('shop:product_list_by_category', args=['test-category'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/index.html')

    def test_product_detail_view(self):
        url = reverse('shop:product_detail', args=[1, 'test-product'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product_detail.html')

    def test_add_to_cart_view(self):
        url = reverse('shop:add_to_cart')
        response = self.client.post(url, {'action': 'add', 'product_id': 1, 'quantity': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.json())

        # Test adding invalid product
        response_invalid_product = self.client.post(url, {'action': 'add', 'product_id': 999, 'quantity': 1})
        self.assertEqual(response_invalid_product.status_code, 404)

    def test_remove_from_cart_view(self):
        url = reverse('shop:remove-from-cart')
        response = self.client.post(url, {'product': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.json())

    def test_shopping_cart_view(self):
        url = reverse('shop:shopping_cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/cart.html')

    def test_create_checkout_session_view(self):
        url = reverse('shop:create-checkout-session')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # You might want to assert more about the response content here, depending on your implementation.

    def test_cancel_checkout_view(self):
        url = reverse('shop:cancel-checkout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancel.html')

    def test_checkout_success_view(self):
        url = reverse('shop:checkout-success')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')
