# Decorators

logged_in = True
user = ''

def requires_login(func):
    new_func = func

    def inner(response, *args, **kwargs):
        # Do stuff
        pass

    print('checking if logged in is true')
    if logged_in == True:
        return new_func
    else:
        try:
            raise UserNotLoggedInException
        except UserNotLoggedInException:
            print('User is not logged in, will return empty func')
            return

class UserNotLoggedInException(Exception):
    def __init__(self):
        pass

@requires_login
def post_comment(response):
    return user + ' says ' + response

user = 'Me'
logged_in = True
print('logged_in is set to true')

try:
    print(post_comment('Hi there (:'))
except TypeError:
    try:
        raise UserNotLoggedInException
    except UserNotLoggedInException:
        print('User is not logged in')
