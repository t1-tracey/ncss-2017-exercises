
def login_required(func, *args, **kwargs):
    def inner(response):
        pass
    return func

@login_required # This is the same as post_comment = login_required(post_comment)
def post_comment(response):
    pass
