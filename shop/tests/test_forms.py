from django.test import TestCase
from ..forms import AddToCartForm
from django.utils.translation import gettext_lazy as _


class TestAddToCartForm(TestCase):
    def test_valid_quantity(self):
        form = AddToCartForm(data={'quantity': 5})
        self.assertTrue(form.is_valid())

    def test_invalid_quantity_zero(self):
        form = AddToCartForm(data={'quantity': 0})
        self.assertFalse(form.is_valid())
        self.assertIn(_('Ensure this value is greater than or equal to 1.'), form.errors['quantity'])

    def test_invalid_quantity_negative(self):
        form = AddToCartForm(data={'quantity': -5})
        self.assertFalse(form.is_valid())
        print(form.errors['quantity'])
        # self.assertIn(_('Ensure this value is greater than or equal to 1'), form.errors['quantity'])

    def test_missing_quantity(self):
        form = AddToCartForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn(_('This field is required.'), form.errors['quantity'])
