def exception_method(number):
    try:
      return 5 / number
    except ZeroDivisionError:
        if ZeroDivisionError:
            return "A number cannot be divide by 0"


print exception_method(0)


