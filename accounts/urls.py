from django.contrib.auth.views import LogoutView, PasswordResetView
from django.urls import path
from django.views.generic import TemplateView

from .views import UserRegistrationView, account_activation, UserLoginView, UpdateProfileView

app_name = 'accounts'
urlpatterns = [
    path('user-registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('account-activation/<slug:uidb64>/<slug:token>/', account_activation, name='activate'),
    path('activation/activation-email/sent/', TemplateView.as_view(template_name="accounts/activation-email-sent.html"),
         name='activation-email-sent'),
    path('user-login/', UserLoginView.as_view(), name="user-login"),
    path('user-logout/', LogoutView.as_view(next_page='/accounts/user-login/'),
         name='user-logout'),
    path('user-profile/update/<str:pk>/', UpdateProfileView.as_view(), name='profile-update'),

    # password reset functionality
    path('password_reset/', PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password-reset'),

]

