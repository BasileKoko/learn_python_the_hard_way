def decorator(f):
    def wrapper():
        print 'before function is called'
        f()
        print 'after function is called'
    return wrapper

@decorator
def sayHello():
    print 'Hello'

sayHello()
