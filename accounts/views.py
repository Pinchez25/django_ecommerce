from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView
from django.contrib.sites.shortcuts import get_current_site
# from django.conf import settings

from .forms import UserRegistrationForm
from .utils import account_activation_token


class UserRegistrationView(FormView):
    template_name = 'accounts/user-registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:activation-email-sent')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(UserRegistrationView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data.get('email')
        user.set_password(form.cleaned_data.get('password'))
        user.is_active = False
        user.save()

        site = get_current_site(request=self.request)
        subject = "Account Activation"
        message = render_to_string(
            'accounts/activate-account.html',
            {
                'user': user,
                'domain': site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            }
        )
        # email_user is a method in the user model that sends message to the current/calling user
        user.email_user(
            subject=subject,
            message=message
            # from_email=settings.EMAIL_HOST_USER
        )
        return super(UserRegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form})


def account_activation(request, uidb64, token):
    try:
        uid = (urlsafe_base64_decode(uidb64)).decode('utf-8')

        user = get_user_model().objects.get(pk=uid)

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/invalid_activation.html', {})

    except ():
        pass
