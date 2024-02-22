from django.shortcuts import render
from functools import wraps
from django.contrib.auth.decorators import user_passes_test


def doctor_role_required(function=None):
    def check_role(user):
        return user.groups.filter(name__in=["Doctor"]).exists()

    actual_decorator = user_passes_test(check_role)

    if function:

        @wraps(function)
        def wrapper(request, *args, **kwargs):
            if not check_role(request.user):
                return render(request, "forbidden_page.html", status=403)
            return function(request, *args, **kwargs)

        return wrapper

    return actual_decorator
