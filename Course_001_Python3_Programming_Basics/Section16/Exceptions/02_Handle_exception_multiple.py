try:
    a = 1
    b = 0
    c = a / b
    print('DEBUG: This will not be executed!')
except ZeroDivisionError as err:
    print(format(err))
except TypeError as err:
    print(format(err))
except Exception as err:
    print(format(err))

print('DEBUG: This will be executed!')
