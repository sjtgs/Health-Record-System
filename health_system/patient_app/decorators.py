from django.http import HttpResponseForbidden
from functools import wraps


# Patient Required Decorators. This function will only users of Patient group to access the specific websites.
def patient_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if (
            request.user.is_authenticated
            and request.user.groups.filter(name="Patient").exists()
        ):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to view this page.")

    return wrapper
