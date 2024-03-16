from django.test import TestCase
from django.urls import reverse
from ..models import Category, Product


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_slug(self):
        category = Category.objects.get(id=1)
        expected_slug = 'test-category'
        self.assertEqual(category.slug, expected_slug)

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        expected_url = reverse('shop:product_list_by_category', args=[category.slug])
        self.assertEqual(category.get_absolute_url(), expected_url)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Test Category')
        Product.objects.create(
            category=category,
            title='Test Product',
            description='Test description',
            price=10.0
        )

    def test_title_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Product Name')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_available_default(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.available)

    def test_created_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('created').verbose_name
        self.assertEqual(field_label, 'created')

    def test_updated_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('updated').verbose_name
        self.assertEqual(field_label, 'updated')

    def test_get_image_url_with_image(self):
        # Create a product with an image
        category = Category.objects.create(name='Test Category 2')
        product = Product.objects.create(
            category=category,
            title='Test Product 2',
            description='Test description 2',
            price=20.0,
            image='test_image.png'  # Provide a non-default image
        )
        print(product.get_image_url())
        self.assertEqual(product.get_image_url(), '/media/test_image.png')

    def test_get_image_url_without_image(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.get_image_url(), '/media/default.png')

    def test_is_available_method(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.is_available())

    def test_str_representation(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), 'Test Product')



