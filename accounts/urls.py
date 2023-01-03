from django.urls import path
from django.views.generic import TemplateView

from .views import UserRegistrationView, account_activation

app_name = 'accounts'
urlpatterns = [
    path('user-registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('account-activation/<slug:uidb64>/<slug:token>/', account_activation, name='activate'),
    path('activation/activation-email/sent/', TemplateView.as_view(template_name="accounts/activation-email-sent.html"),
         name='activation-email-sent'),
]
