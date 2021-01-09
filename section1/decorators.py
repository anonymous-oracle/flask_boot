import functools

user = {'username': 'jose', 'access_level': 'guest'}


# return password according to the access level
# if access level is guest then the password won't be returned
def make_secure(func):
    # the below line makes sure that the secure_function() only acts as a wrapper to whatever
    # "func" function was passed to it without replacing func's registry
    @functools.wraps(func)
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'no admin permissions for %s' % (user['username'])
    return secure_function


@make_secure
def get_admin_password():
    return '1234'


# get_admin_password = make_secure(get_admin_password)

print(get_admin_password())

# without using functools, the properties of the get_admin_password function will be lost
# it will not be registered as 'get_admin_password()'; run the below line without functool functionality
# to see what i mean
print(get_admin_password.__name__)
