import functools

user = {'username': 'anonymous', 'access_level': 'guest'}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f'no %s permissions for %s' % (access_level ,user['username'])
        return secure_function
    return decorator


@make_secure(user['access_level'])
def get_admin_password():
    return '1234'


@make_secure('admin')
def get_guest_password():
    return 'password'


print(get_admin_password())
print(get_guest_password())
