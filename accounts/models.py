from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):

    # should accept username field plus all other required fields as args
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                _('Superuser must be assigned to is_staff=True')
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Superuser must be assigned to is_superuser=True')
            )
        if other_fields.get('is_active') is not True:
            raise ValueError(
                _('Superuser must be assigned to is_active=True')
            )

        return self.create_user(email, username, password, **other_fields)

    """
       The create_user() must accept the username field (USERNAME_FIELD) of the user model
       plus all the other required fields as arguments.
       
       The custom user model below defines 'email' as the username field and 'username' field
       as a required field. password is by default required.
    """

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('Email address is required'))

        # normalize_email() lowercases the domain portion of the email address
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)

        user.set_password(password)
        user.save()

        return user


class Account(AbstractUser):
    email = models.EmailField(_('Email'), unique=True)
    username = models.CharField(_('username'), max_length=150, unique=True)
    first_name = models.CharField(_('firstname'), max_length=150, blank=True)
    bio = models.TextField(_('Bio'), max_length=500, blank=True)
    image = models.ImageField(_('Image'), upload_to='profile/', default='default.jpg')
    country = CountryField(_('country'), blank_label=_('----------select country----------'))
    contact = PhoneNumberField(_('Contact'), blank=True)
    postal_address = models.CharField(max_length=50, blank=True, verbose_name=_('Postal Address'))
    address = models.CharField(_('address'), max_length=120, blank=True)
    city = models.CharField(_('City'), max_length=120, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    # Describes the field of the model that is used as the unique identifier
    USERNAME_FIELD = 'email'
    
    """
        REQUIRED_FIELDS specify field names to be prompted when creating
        a user using the createsuperuser management command.
    """
    # NB: REQUIRED_FIELDS should not contain the USERNAME_FIELD or password
    # as these will always be prompted for.
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('Accounts')
        verbose_name_plural = _('Accounts')

    def __str__(self):
        return self.username
