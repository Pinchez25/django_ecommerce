from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.utils.translation import gettext_lazy as _
from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(step_size=1, min_value=1, label=_('quantity'))

    def __init__(self, *args, **kwargs):
        super(AddToCartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            'quantity',
            Submit('submit', _('Add to Cart'), css_class='btn btn-primary btn-user btn-block btnAddToCart')
        )
        self.fields['quantity'].widget.attrs.update({'id': 'item-quantity'})

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')

        if not quantity:
            raise forms.ValidationError(_(f'Please enter the quantity'))
        elif quantity < 0 or quantity == 0:
            raise forms.ValidationError(_('Quantity has to be greater than 0'))

        return quantity

    def get_initial_for_field(self, field, field_name):
        if field_name == 'quantity':
            return 1
        return super(AddToCartForm, self).get_initial_for_field(field, field_name)
