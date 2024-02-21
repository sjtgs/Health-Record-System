from django.http import HttpResponseForbidden
from functools import wraps


# Nurse Required Decorators. This function will only users of Nurse group to access the specific websites
def nurse_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if (
            request.user.is_authenticated
            and request.user.groups.filter(name="Nurse").exists()
        ):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to view this page.")

    return wrapper
