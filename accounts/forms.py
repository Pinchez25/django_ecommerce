from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(
        label=_('Confirm Password'),
        min_length=4,
        max_length=50,
        help_text=_('Please confirm your password...'),
        widget=forms.PasswordInput()
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']
        help_texts = {
            'username': _('Enter username...'),
            'password': _('Your password...'),
            'email': _('Enter your email address...'),
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            Row(
                Column('password'),
                Column('password2'),
            ),
            Row(
                Submit('submit', 'Register', css_class='btn btn-success', css_id='btnRegister'),
                css_class='text-center'
            )
        )
        self.fields['password'].widget.attrs.update({'id': 'user-password'})

    def clean_username(self):
        username = str(self.cleaned_data.get('username')).lower()

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError(_('Username already exists'))

        return username

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError(_('Password mismatch!'))
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(_('Email already exists'))

        return email
