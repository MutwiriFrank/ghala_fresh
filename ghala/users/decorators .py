from django.http import HttpResponse
from django.shortcuts import redirect

# to be placed on top of login and register, to send already authenticated users to a specific page


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func