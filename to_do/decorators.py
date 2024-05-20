from functools import wraps
from django.http import JsonResponse

def custom_decorator(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        # Add custom behavior here
        print("Custom decorator logic before view execution")
        response = func(*args, **kwargs)
        print("Custom decorator logic after view execution")
        return response
    return wrapped_func
