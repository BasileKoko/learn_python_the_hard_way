def decorator(f):
    def wrapper(*args, **kwargs):
        print 'before function is called'
        f(*args, **kwargs)
        print 'after function is called'
    return wrapper

@decorator
def sayHello(name):
    print name

sayHello('Tom')
