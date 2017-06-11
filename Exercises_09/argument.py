def argument(*args):
    for i in args:
        print(i)

argument(1, 4, 3, 7)


def keyword_argument(**kwargs):
    for i in kwargs:
        print(kwargs[i])

keyword_argument(x=10, y=20, z=28)
