from functools import wraps


def require_view(attr_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if getattr(self, attr_name, None) is None:
                return None
            return func(self, *args, **kwargs)

        return wrapper

    return decorator
