# custom login required decorator

from functools import wraps

from django.shortcuts import redirect


def login_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            return redirect('accounts:user-login')

    return wrap


# As a class-based mixin
class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def admin_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_admin:
            return function(request, *args, **kwargs)
        else:
            return redirect('accounts:user-login')

    return wrap

class AdminRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AdminRequiredMixin, cls).as_view(**initkwargs)
        return admin_only(view)
