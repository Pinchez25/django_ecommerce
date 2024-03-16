from crispy_forms.bootstrap import StrictButton
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            Row(
                # Submit('submit', _('Login'), css_class='btn btn-success', css_id='btnLogin'),
                StrictButton(_('Login'), type='submit', css_class='btn btn-outline-info', css_id='btnLogin'),
                css_class='text-center'
            )
        )
        # add w-100 class to username and password fields
        self.fields['username'].widget.attrs.update({'class': 'w-100'})
        self.fields['password'].widget.attrs.update({'class': 'w-100'})


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
                StrictButton(_('Register'), type='submit', css_class='btn btn-outline-info', css_id='btnRegister'),
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


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'image', 'bio', 'country', 'contact', 'postal_address', 'address',
                  'city']
        help_texts = {
            'first_name': _('Specify your firstname'),
            'last_name': _('Specify your lastname'),
            'bio': _('Tell us about your self'),
            'country': _('Specify your country'),
            'contact': _('Enter your phone number'),
            'postal_address': _('Specify your postal address'),
            'address': _('Specify your residence'),
            'city': _('Specify your city'),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            Row(
                Column('first_name'),
                Column('last_name'),
            ),
            'image',
            'contact',
            'country',
            'bio',
            'postal_address',
            'address',
            'city',
            Row(
                # Submit('submit', 'Update Profile', css_class='btn btn-success', css_id='btnProfileUpdate'),
                StrictButton(_('Update Profile'), type='submit', css_class='btn btn-outline-info',
                             css_id='btnProfileUpdate'),
                css_class='text-center'
            )
        )

        self.fields['email'].widget.attrs['readonly'] = True

    def clean_country(self):
        country = self.cleaned_data.get('country')

        if not country or country == "":
            raise forms.ValidationError(_('Country Field is required'))

        return country
